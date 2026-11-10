import time
from pathlib import Path

ARCHIVO_ENTRADA = Path("../Comunicacion/entrada_servidor.txt")
ARCHIVO_SALIDA = Path("../Comunicacion/salida_servidor.txt")


def enviar_mensaje():
    mensaje = input("\nEscribe un mensaje: ")

    # Verificar que el usuario haya escrito algo
    if not mensaje.strip():
        print("No se puede enviar un mensaje vacío.")
        return

    # Escribir mensaje en el archivo de entrada
    ARCHIVO_ENTRADA.write_text(
        mensaje,
        encoding="utf-8"
    )

    print("Mensaje enviado.")
    print("Esperando respuesta del servidor...")

    # Simular latencia
    time.sleep(2)

    # Esperar hasta que exista una respuesta
    while True:
        respuesta = ARCHIVO_SALIDA.read_text(
            encoding="utf-8"
        ).strip()

        if respuesta:
            print(f"Respuesta del servidor: {respuesta}")

            # Limpiar respuesta después de leerla
            ARCHIVO_SALIDA.write_text(
                "",
                encoding="utf-8"
            )

            break

        time.sleep(1)


print("Cliente iniciado.")

while True:
    enviar_mensaje()

    continuar = input("\n¿Deseas enviar otro mensaje? (s/n): ")

    if continuar.lower() != "s":
        print("Cliente finalizado.")
        break