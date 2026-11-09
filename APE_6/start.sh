#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

# Detectar motor de contenedores disponible (Docker o Podman)
if command -v docker >/dev/null 2>&1; then
  ENGINE="docker"
elif command -v podman >/dev/null 2>&1; then
  ENGINE="podman"
else
  echo "ERROR: se requiere Docker o Podman para levantar RabbitMQ."
  exit 1
fi

echo "==> Usando $ENGINE para RabbitMQ"

# Levantar RabbitMQ (si ya existe el contenedor, solo se inicia)
if "$ENGINE" ps -a --format '{{.Names}}' | grep -qx 'rabbitmq_broker'; then
  "$ENGINE" start rabbitmq_broker >/dev/null 2>&1 || true
else
  "$ENGINE" run -d \
    --name rabbitmq_broker \
    -p 5672:5672 \
    -p 15672:15672 \
    -e RABBITMQ_DEFAULT_USER=admin \
    -e RABBITMQ_DEFAULT_PASS=admin123 \
    --restart unless-stopped \
    docker.io/library/rabbitmq:3-management
fi

echo "==> Esperando a que RabbitMQ acepte conexiones..."
for i in $(seq 1 60); do
  if (exec 3<>/dev/tcp/127.0.0.1/5672) 2>/dev/null; then
    exec 3>&- || true
    echo "    RabbitMQ listo."
    break
  fi
  sleep 2
done

echo "==> Compilando proyecto"
mvn clean package -DskipTests

echo "==> Iniciando Fleet Monitor"
exec java -jar target/fleet-monitor-1.0.0-SNAPSHOT.jar
