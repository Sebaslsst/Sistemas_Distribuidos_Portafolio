import json
import socket
import sys


def servidor_base(puerto, host="0.0.0.0"):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
        servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        servidor.bind((host, puerto))
        servidor.listen()
        print(f"[WORKER {host}:{puerto}] activo...")

        while True:
            conn, addr = servidor.accept()
            with conn:
                try:
                    data = conn.recv(4096)
                    if data:
                        pedido = json.loads(data.decode())
                        print(f"[WORKER {puerto}] Recibido de {addr}:", pedido)
                except (json.JSONDecodeError, UnicodeDecodeError) as error:
                    print(f"[WORKER {puerto}] Mensaje invalido:", error)


if __name__ == "__main__":
    servidor_base(int(sys.argv[1]))
