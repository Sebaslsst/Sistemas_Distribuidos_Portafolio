import time
from pathlib import Path

# Ruta del archivo de entrada y salida
ARCHIVO_ENTRADA = Path("../Comunicacion/entrada_servidor.txt")
ARCHIVO_SALIDA = Path("../Comunicacion/salida_servidor.txt")


def procesar_mensaje(mensaje):
    """Convierte el mensaje recibido a mayúsculas."""
    return mensaje.upper()


print("Servidor iniciado...")
print("Esperando mensajes...")


while True:
    try:
        # Verificar que exista el archivo
        if ARCHIVO_ENTRADA.exists():

            # Leer el contenido
            mensaje = ARCHIVO_ENTRADA.read_text(encoding="utf-8").strip()

            # Si hay contenido, procesarlo
            if mensaje:
                print(f"Mensaje recibido: {mensaje}")

                # Procesar mensaje
                respuesta = procesar_mensaje(mensaje)

                # Escribir respuesta
                ARCHIVO_SALIDA.write_text(
                    respuesta,
                    encoding="utf-8"
                )

                print(f"Respuesta enviada: {respuesta}")

                # Vaciar el archivo de entrada
                ARCHIVO_ENTRADA.write_text("", encoding="utf-8")

        # Revisar nuevamente después de 1 segundo
        time.sleep(1)

    except KeyboardInterrupt:
        print("\nServidor detenido.")
        break

    except Exception as e:
        print(f"Error: {e}")
        time.sleep(1)