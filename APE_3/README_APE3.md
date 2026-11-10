# APE 3 - Concurrencia y sincronización

Implementación de cinco ejercicios de concurrencia mediante microservicios independientes desarrollados con Spring Boot y una interfaz web que permite visualizar y ejecutar las simulaciones.

## Tecnologías

- Java 25 (LTS)
- Spring Boot
- Maven 3.9+
- JavaScript y Vite
- Semáforos, mutex, locks y condiciones

## Ejercicios implementados

- **Ejercicio 1:** control de un estacionamiento mediante un semáforo contador, con capacidad configurable para vehículos. Puerto `8081`.
- **Ejercicio 2:** simulación bancaria con un mutex justo para proteger el saldo durante operaciones concurrentes. Puerto `8082`.
- **Ejercicio 3:** problema productor-consumidor mediante `LinkedBlockingQueue`, semáforos y sincronización del estado.
- **Ejercicio 4:** control de un puente de una sola vía mediante `ReentrantLock(true)` y `Condition`.
- **Ejercicio 5:** coordinación secuencial de diseño, revisión e impresión de documentos utilizando semáforos. Puerto `8085`.

## Ejecución

### 1. Requisitos

Tener instalados Java 25, Maven 3.9 o posterior y Node.js con npm.

### 2. Iniciar los microservicios

Desde la carpeta `APE_3`, ejecutar:

```bash
for dir in ejercicio-1 ejercicio-2 ejercicio-3 ejercicio-4 ejercicio-5; do
  (cd "$dir" && mvn spring-boot:run) &
done
wait
```

Este comando inicia los cinco microservicios en segundo plano dentro de la misma terminal.

### 3. Iniciar el frontend

Abrir otra terminal desde `APE_3`:

```bash
cd frontend
npm install
npm run dev
```

### 4. Acceder al sistema

Abrir en el navegador la dirección indicada por Vite, normalmente:

http://localhost:5173

Desde la interfaz web se puede seleccionar cualquiera de los cinco ejercicios, configurar sus parámetros y observar los resultados de las simulaciones.

## Resultado esperado

- Ejecución independiente de los cinco microservicios.
- Control del acceso concurrente a recursos compartidos.
- Sincronización de hilos mediante semáforos, mutex y locks.
- Visualización de estados y eventos desde el frontend.

## Propósito académico

Comprender los mecanismos de concurrencia y sincronización en sistemas distribuidos, evitando condiciones de carrera y coordinando correctamente la ejecución de procesos y tareas.
