import socket
import json
import os
import threading

from agente_ia import decision_ia

HOST = "0.0.0.0"
PORT = 6000



def cargar_servidores():
    configuracion = os.getenv("WORKERS", "127.0.0.1:7001,127.0.0.1:7002")
    servidores_configurados = []
    for worker in configuracion.split(","):
        host, puerto = worker.strip().rsplit(":", 1)
        servidores_configurados.append((host, int(puerto)))
    return servidores_configurados


servidores = cargar_servidores()
indice = 0
lock = threading.Lock()


def enviar(destino, data):
    try:
        with socket.create_connection(destino, timeout=5) as s:
            s.sendall(json.dumps(data).encode())

        print("[GATEWAY] Enviado a", destino)
    except Exception as e:
        print("[ERROR GATEWAY]", e)


def manejar_cliente(conn, addr):
    global indice

    try:
        data = conn.recv(4096)

        if data:
            decoded = json.loads(data.decode())

            idx = decision_ia(decoded)

            if idx is None:
                with lock:
                    idx = indice
                    indice = (indice + 1) % len(servidores)

            destino = servidores[idx]

            print("[GATEWAY] Cliente", addr, "->", destino)

            enviar(destino, decoded)
    except (json.JSONDecodeError, KeyError, IndexError, ValueError) as error:
        print("[ERROR GATEWAY] Mensaje invalido:", error)

    conn.close()


def gateway():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen()

    print("[GATEWAY] activo...")

    while True:
        conn, addr = s.accept()
        thread = threading.Thread(target=manejar_cliente, args=(conn, addr))
        thread.start()


if __name__ == "__main__":
    gateway()