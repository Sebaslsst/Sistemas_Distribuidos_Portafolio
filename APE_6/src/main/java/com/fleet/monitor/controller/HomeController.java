package com.fleet.monitor.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

@RestController
public class HomeController {

    @GetMapping("/")
    public Map<String, Object> home() {
        Map<String, Object> info = new LinkedHashMap<>();
        info.put("application", "Fleet Monitor");
        info.put("status", "running");
        info.put("endpoints", List.of(
                "/api/fleet/status",
                "/api/fleet/vehicle/{id}/telemetria",
                "/h2-console"
        ));
        info.put("rabbitmqManagement", "http://127.0.0.1:15672");
        return info;
    }
}
