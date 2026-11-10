import socket
import json
import os
import time

def cliente(memoria):
    HOST = os.getenv("GATEWAY_HOST", "127.0.0.1")
    PORT = int(os.getenv("GATEWAY_PORT", "6000"))

    while True:
        if "data" in memoria:
            data = memoria["data"]

            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((HOST, PORT))
                s.send(json.dumps(data).encode())
                s.close()

                print("[CLIENTE] Enviado:", data)
            except:
                print("[CLIENTE] Error conexión")

        time.sleep(2)