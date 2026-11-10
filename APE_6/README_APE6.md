
# APE 6 - Microservicios con RabbitMQ y Spring Boot

Implementación de un sistema de procesamiento de telemetría vehicular mediante RabbitMQ y Spring Boot, como continuación de la práctica APE 5.

El proyecto permite recibir mensajes GPS, procesar alertas de temperatura y combustible, almacenar información y consultar los registros mediante una API REST.

## Tecnologías

- Java 17 o superior
- Spring Boot 3.2
- Spring AMQP
- RabbitMQ
- Docker y Docker Compose
- Maven
- Spring Data JPA y H2 Database

## Componentes del proyecto

- `RabbitMQConfig.java`: configura el exchange Direct, las colas durables y los bindings.
- `GpsConsumer.java`: recibe y procesa los mensajes GPS.
- `GpsMessage.java`: representa los datos de telemetría.
- `GpsMessageRepository.java`: almacena y consulta registros mediante JPA.
- `AlertConsumer.java`: procesa alertas de temperatura y combustible y las reenvía a notificaciones.
- `FleetController.java`: expone los endpoints REST.
- `application.properties`: contiene la configuración de RabbitMQ, H2 y Spring Boot.

## Ejecución

### 1. Requisitos

Tener instalados Java, Maven y Docker con Docker Compose.

### 2. Iniciar RabbitMQ

Desde la carpeta `APE_6`:

```bash
docker compose -f docker-compose-rabbitmq.yml up -d
```

Verificar el contenedor:

```bash
docker ps
```

La interfaz de RabbitMQ estará disponible en:

http://localhost:15672

Credenciales predeterminadas del archivo Docker Compose:

- Usuario: `admin`
- Contraseña: `admin123`

Verificar que estas credenciales coincidan con las configuradas en `application.properties`.

### 3. Ejecutar Spring Boot

En otra terminal, desde `APE_6`:

```bash
mvn spring-boot:run
```

La aplicación estará disponible en el puerto `8080`.

También se puede utilizar el script incluido en Linux:

```bash
./start.sh
```

Este script prepara RabbitMQ, compila el proyecto y ejecuta Fleet Monitor.

### 4. Consultar la API REST

Estado general de la flota:

```bash
curl http://localhost:8080/api/fleet/status
```

Consultar la telemetría de un vehículo:

```bash
curl http://localhost:8080/api/fleet/vehicle/VH-001/telemetria
```

La segunda consulta devuelve un arreglo JSON con los registros GPS almacenados. Si todavía no se han recibido mensajes, devuelve `[]`.

### 5. Probar el consumidor GPS

Desde la interfaz de RabbitMQ:

1. Entrar en `Exchanges`.
2. Seleccionar `exchange.fleet`.
3. Abrir la sección `Publish message`.
4. Escribir `gps.routing` como routing key.
5. Publicar el siguiente JSON:

```json
{
  "vehicleId": "VH-001",
  "timestamp": "2026-11-08T20:45:00",
  "lat": -3.9931,
  "lng": -79.2042,
  "speed": 45.5
}
```

Después, consultar nuevamente:

```bash
curl http://localhost:8080/api/fleet/vehicle/VH-001/telemetria
```

Si el consumidor procesa correctamente el mensaje, el registro aparecerá en la respuesta.

## Resultado esperado

- Configuración de RabbitMQ con colas durables y un exchange Direct.
- Recepción y procesamiento de mensajes GPS.
- Almacenamiento de telemetría mediante Spring Data JPA y H2.
- Procesamiento de alertas de temperatura y combustible.
- Reenvío de alertas hacia una cola de notificaciones.
- Consulta de información mediante una API REST.

## Consideraciones

- La base de datos H2 está configurada en memoria, por lo que sus registros se pierden al reiniciar la aplicación.
- El endpoint `/api/fleet/status` utiliza valores fijos para vehículos y alertas; no representa estadísticas dinámicas.
- Los puertos `5672`, `15672` y `8080` deben estar disponibles.
- La ejecución predeterminada utiliza `localhost`. Para distribuir los servicios entre varias computadoras es necesario adaptar las direcciones IP y la configuración de red.
- No se debe ejecutar simultáneamente otro contenedor RabbitMQ que utilice los mismos puertos.

## Propósito académico

Comprender la integración de RabbitMQ con Spring Boot mediante comunicación asíncrona, procesamiento de mensajes, persistencia de telemetría y exposición de servicios REST.
