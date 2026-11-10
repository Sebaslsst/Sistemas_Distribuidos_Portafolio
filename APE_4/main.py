import os
import signal
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
PROCESOS = [
    ([sys.executable, "worker.py", "7001"], ROOT / "servidores-system"),
    ([sys.executable, "worker.py", "7002"], ROOT / "servidores-system"),
    ([sys.executable, "gateway.py"], ROOT / "gateway-system"),
    ([sys.executable, "app.py"], ROOT / "cliente_system"),
]


def main():
    procesos = []
    try:
        for comando, directorio in PROCESOS:
            procesos.append(subprocess.Popen(comando, cwd=directorio))
        print("[MAIN] Sistema integrado activo. Presiona Ctrl+C para detenerlo.")
        for proceso in procesos:
            proceso.wait()
    except KeyboardInterrupt:
        print("\n[MAIN] Deteniendo el sistema...")
    finally:
        for proceso in procesos:
            if proceso.poll() is None:
                proceso.terminate()
        for proceso in procesos:
            proceso.wait()


if __name__ == "__main__":
    main()
