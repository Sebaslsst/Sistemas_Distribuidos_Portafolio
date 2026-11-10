
# Portafolio de Sistemas Distribuidos

Repositorio académico de las prácticas desarrolladas en la asignatura de **Sistemas Distribuidos**, correspondiente al sexto ciclo de la carrera de Computación de la Universidad Nacional de Loja.

Las actividades abarcan comunicación cliente-servidor, concurrencia, comunicación entre procesos, arquitectura distribuida, mensajería asíncrona y desarrollo de servicios utilizando Python, Java, Spring Boot, MQTT y RabbitMQ.

## Link con los reportes de las prácticas
https://drive.google.com/drive/folders/1E5HgL2HcdklDPPOi2DqGj6l1P2xhos7a?usp=sharing

## Prácticas desarrolladas

### APE 2 - Comunicación cliente-servidor

Implementación de mecanismos de comunicación entre un cliente y un servidor mediante programas desarrollados en Python y Java.

El proyecto contiene:

- `Cliente/cliente.py`: implementación del cliente.
- `Servidor/servidor.py`: implementación del servidor.
- `Comunicacion/`: archivos utilizados para el intercambio de información.
- `Practica2.java`: programa desarrollado en Java.

**Tecnologías:** Python y Java.

### APE 3 - Concurrencia y sincronización

Implementación de cinco ejercicios de concurrencia mediante microservicios independientes con Spring Boot y una interfaz web desarrollada con Vite.

- **Ejercicio 1:** semáforo contador para controlar el acceso de vehículos a un estacionamiento.
- **Ejercicio 2:** mutex justo para proteger operaciones bancarias concurrentes.
- **Ejercicio 3:** problema productor-consumidor utilizando `LinkedBlockingQueue` y semáforos.
- **Ejercicio 4:** control del acceso a un puente mediante `ReentrantLock` y `Condition`.
- **Ejercicio 5:** coordinación de tareas mediante semáforos encadenados.

**Tecnologías:** Java 25, Spring Boot, Maven, JavaScript y Vite.

### APE 4 - Arquitectura distribuida e IPC

Desarrollo de un sistema distribuido compuesto por clientes, servidores y un gateway de comunicación.

El proyecto incluye:

- `cliente_system/`: implementación del cliente.
- `servidores-system/`: servidores y procesos de trabajo.
- `gateway-system/`: componentes de intermediación y agente de IA.
- `ipc_system/`: mecanismos de comunicación entre procesos.
- `main.py`: archivo principal del proyecto.
- `requirements.txt`: dependencias de Python.

**Tecnologías:** Python, comunicación IPC y arquitectura cliente-servidor.

### APE 5 - Mensajería distribuida con MQTT y RabbitMQ

Implementación de un sistema de simulación de sensores IoT para el monitoreo de una flota vehicular.

- Simulación de datos GPS, temperatura y combustible.
- Publicación y suscripción de mensajes mediante MQTT.
- Configuración del broker Mosquitto.
- Integración de MQTT con RabbitMQ mediante un servicio puente.
- Almacenamiento de telemetría mediante SQLite.
- Scripts de pruebas y verificación de resultados.

**Tecnologías:** Python, MQTT, Mosquitto, RabbitMQ, Docker y SQLite.

### APE 6 - Microservicios con RabbitMQ y Spring Boot

Implementación de componentes para recibir y procesar mensajes de telemetría vehicular mediante RabbitMQ y Spring Boot.

- Configuración de un exchange Direct y colas durables.
- Implementación de consumidores GPS mediante `@RabbitListener`.
- Procesamiento de alertas de temperatura y combustible.
- Reenvío de mensajes hacia una cola de notificaciones.
- Almacenamiento de registros GPS mediante Spring Data JPA y H2.
- Exposición de endpoints REST para consultar información de la flota.

**Tecnologías:** Java, Spring Boot, Spring AMQP, RabbitMQ, Maven, Docker y H2.

## Estructura del repositorio

```text
Sistemas_Distribuidos_Portafolio/
├── APE_2/
├── APE_3/
├── APE_4/
├── APE_5/
├── APE_6/
└── README.md
```

Cada carpeta contiene el código fuente y los archivos de configuración correspondientes a su práctica.

## Tecnologías utilizadas

- **Lenguajes:** Python, Java y JavaScript.
- **Frameworks:** Spring Boot y Spring Data JPA.
- **Mensajería:** MQTT, AMQP, Mosquitto y RabbitMQ.
- **Infraestructura:** Docker y Docker Compose.
- **Bases de datos:** SQLite y H2.
- **Comunicación:** IPC, HTTP, API REST y arquitectura cliente-servidor.
- **Herramientas:** Maven, Git, GitHub y Vite.

## Objetivo del portafolio

Documentar las actividades práctico-experimentales desarrolladas durante la asignatura de Sistemas Distribuidos, aplicando conceptos de concurrencia, sincronización, comunicación entre procesos e integración de servicios.

## Autor

**Leonardo Sebastian Sámchez Torres**  
Carrera de Computación  
Universidad Nacional de Loja

## Uso académico

Este repositorio contiene proyectos desarrollados con fines académicos. Algunas actividades corresponden a trabajos grupales y otras a implementaciones individuales.

El código y los archivos de configuración se encuentran organizados por práctica para facilitar su revisión y ejecución.

