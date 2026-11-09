package com.fleet.monitor.consumer;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.fleet.monitor.config.RabbitMQConfig;
import com.fleet.monitor.model.GpsMessage;
import com.fleet.monitor.repository.GpsMessageRepository;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.amqp.rabbit.annotation.RabbitListener;
import org.springframework.stereotype.Component;

@Component
public class GpsConsumer {

    private static final Logger log = LoggerFactory.getLogger(GpsConsumer.class);

    private final GpsMessageRepository gpsMessageRepository;
    private final ObjectMapper objectMapper;

    public GpsConsumer(GpsMessageRepository gpsMessageRepository, ObjectMapper objectMapper) {
        this.gpsMessageRepository = gpsMessageRepository;
        this.objectMapper = objectMapper;
    }

    @RabbitListener(queues = RabbitMQConfig.GPS_QUEUE)
    public void consumeGps(String message) {
        try {
            log.info("GPS recibido: {}", message);

            GpsMessage gpsMessage = objectMapper.readValue(message, GpsMessage.class);
            gpsMessageRepository.save(gpsMessage);

            log.info("GPS almacenado en BD para el vehiculo {}", gpsMessage.getVehicleId());
        } catch (Exception e) {
            log.error("Error procesando GPS: {}", e.getMessage());
        }
    }
}
