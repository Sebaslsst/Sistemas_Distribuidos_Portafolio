
# APE 5 - Mensajería distribuida con MQTT y RabbitMQ

Implementación de un sistema de monitoreo de flotas vehiculares mediante sensores IoT simulados. El proyecto utiliza MQTT para transmitir datos de telemetría, RabbitMQ para distribuir mensajes y SQLite para almacenar la información.

## Tecnologías

- Python 3.10 o superior
- MQTT y Eclipse Mosquitto
- RabbitMQ (AMQP)
- Docker y Docker Compose
- SQLite
- paho-mqtt y pika

## Componentes del proyecto

- `simulador_sensores.py`: simula datos GPS, temperatura y combustible de tres vehículos.
- `suscriptor_sqlite.py`: recibe mensajes MQTT y almacena la telemetría en SQLite.
- `mqtt_rabbitmq_bridge.py`: conecta MQTT con RabbitMQ y distribuye mensajes.
- `prueba_alertas.py`: genera mensajes de prueba.
- `verificar_resultados.py`: permite consultar los registros almacenados.
- `docker-compose.yml`: configura Mosquitto y RabbitMQ.

## Ejecución

### 1. Instalar dependencias

Desde la carpeta `APE_5`:

```bash
python3 -m pip install -r requirements.txt
```

### 2. Iniciar Mosquitto y RabbitMQ

```bash
docker compose up -d
```

Verificar los contenedores:

```bash
docker compose ps
```

### 3. Ejecutar los servicios

Abrir tres terminales independientes desde `APE_5`.

**Terminal 1 - Suscriptor MQTT y SQLite:**

```bash
python3 suscriptor_sqlite.py
```

**Terminal 2 - Puente MQTT-RabbitMQ:**

```bash
python3 mqtt_rabbitmq_bridge.py
```

**Terminal 3 - Simulador de sensores:**

```bash
python3 simulador_sensores.py --rondas 2
```

### 4. Verificar los resultados

En otra terminal:

```bash
python3 verificar_resultados.py
```

Para realizar una prueba controlada de alertas:

```bash
python3 prueba_alertas.py
```

### 5. Acceder a RabbitMQ

Abrir en el navegador:

http://localhost:15672

Credenciales predeterminadas del proyecto:

- Usuario: `guest`
- Contraseña: `guest`

Desde la interfaz de administración se pueden revisar las colas GPS, temperatura y combustible.

## Resultado esperado

- Publicación de datos simulados de tres vehículos.
- Recepción de mensajes mediante MQTT.
- Almacenamiento de telemetría en SQLite.
- Transferencia de mensajes desde MQTT hacia RabbitMQ.
- Generación de alertas por temperatura superior a 4 °C y combustible inferior al 20 %.
- Verificación de los registros y las colas de mensajería.

## Detener los servicios

```bash
docker compose down
```

## Propósito académico

Comprender la comunicación asíncrona entre componentes distribuidos mediante MQTT y AMQP, integrando simulación de sensores, procesamiento de mensajes y almacenamiento de información.
