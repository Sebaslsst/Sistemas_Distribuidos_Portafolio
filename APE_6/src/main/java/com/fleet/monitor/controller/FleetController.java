package com.fleet.monitor.controller;

import com.fleet.monitor.model.GpsMessage;
import com.fleet.monitor.repository.GpsMessageRepository;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.Date;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/api/fleet")
public class FleetController {

    private final GpsMessageRepository gpsMessageRepository;

    public FleetController(GpsMessageRepository gpsMessageRepository) {
        this.gpsMessageRepository = gpsMessageRepository;
    }

    @GetMapping("/status")
    public ResponseEntity<Map<String, Object>> getFleetStatus() {
        Map<String, Object> status = new HashMap<>();
        status.put("totalVehicles", 3);
        status.put("activeAlerts", 2);
        status.put("timestamp", new Date());
        return ResponseEntity.ok(status);
    }

    @GetMapping("/vehicle/{id}/telemetria")
    public ResponseEntity<List<GpsMessage>> getTelemetria(@PathVariable String id) {
        return ResponseEntity.ok(gpsMessageRepository.findByVehicleIdOrderByIdAsc(id));
    }
}
