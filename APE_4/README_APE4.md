
# APE 4 - Arquitectura distribuida e IPC

Implementación de un sistema distribuido en Python que integra clientes, servidores, un gateway de comunicación y mecanismos de comunicación entre procesos (IPC).

El proyecto organiza diferentes componentes para gestionar solicitudes y coordinar el intercambio de información.

## Tecnologías

- Python 3
- Arquitectura cliente-servidor
- Comunicación entre procesos (IPC)
- Gateway de comunicación
- Procesamiento distribuido

## Componentes del proyecto

- **Cliente:** `cliente_system/cliente.py` y `app.py`, componentes del sistema cliente.
- **Gateway:** `gateway-system/gateway.py`, intermediario de comunicación entre componentes.
- **Agente de IA:** `gateway-system/agente_ia.py`, módulo destinado a funciones relacionadas con inteligencia artificial.
- **Servidores:** `servidores-system/server.py` y `worker.py`, componentes de procesamiento.
- **IPC:** `productor.py` y `procesador.py`, módulos para la comunicación entre procesos.

## Ejecución

### 1. Requisitos

Tener instalado Python 3 y pip.

### 2. Instalar dependencias

Desde la carpeta `APE_4`:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3. Configurar el entorno

El proyecto incluye un archivo `.env.example` como referencia para las variables de configuración.

```bash
cp .env.example .env
```

Revisar y completar los valores necesarios antes de iniciar la aplicación.

### 4. Iniciar el proyecto

Desde la carpeta `APE_4`:

```bash
python3 main.py
```

El proyecto también contiene componentes independientes de cliente, gateway y servidores que pueden requerir procesos separados según su configuración.

## Resultado esperado

- Ejecución de los componentes del sistema distribuido.
- Comunicación entre clientes, gateway y servidores.
- Intercambio de información entre procesos.
- Coordinación de operaciones entre los módulos implementados.

## Propósito académico

Comprender la organización de una arquitectura distribuida y el funcionamiento de los mecanismos de comunicación e intercambio de información entre procesos y servicios.
