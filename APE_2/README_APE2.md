# APE 2 - Comunicación entre procesos y concurrencia

Implementación de ejercicios de Sistemas Distribuidos utilizando Python y Java. Se trabaja con comunicación cliente-servidor mediante archivos compartidos y sincronización de hilos mediante mutex.

## Tecnologías

- Python 3
- Java
- Comunicación mediante archivos
- Hilos y ReentrantLock

## Ejecución

### 1. Comunicación cliente-servidor (Python)

Desde la carpeta `APE_2`, abrir dos terminales.

**Terminal 1 - Servidor:**

```bash
cd Servidor
python3 servidor.py
```

**Terminal 2 - Cliente:**

```bash
cd Cliente
python3 cliente.py
```

El cliente permite escribir mensajes que son enviados mediante `entrada_servidor.txt`. El servidor procesa el mensaje, lo convierte a mayúsculas y devuelve el resultado mediante `salida_servidor.txt`.

### 2. Concurrencia con mutex (Java)

El archivo `Practica2.java` contiene la clase `CajeroAutomatico`, que simula operaciones bancarias concurrentes.

Para ejecutarlo, el archivo debe llamarse `CajeroAutomatico.java`, porque contiene una clase pública con ese nombre.

```bash
cp Practica2.java CajeroAutomatico.java
javac CajeroAutomatico.java
java CajeroAutomatico
```

## Resultado esperado

- Intercambio de mensajes entre cliente y servidor.
- Procesamiento de mensajes y devolución de respuestas.
- Sincronización de operaciones bancarias mediante ReentrantLock.
- Protección del saldo compartido frente a accesos concurrentes.

## Propósito académico

Comprender mecanismos de comunicación entre procesos y aplicar herramientas de sincronización para evitar conflictos durante la ejecución concurrente.
