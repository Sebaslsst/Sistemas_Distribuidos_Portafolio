package com.fleet.monitor.repository;

import com.fleet.monitor.model.GpsMessage;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface GpsMessageRepository extends JpaRepository<GpsMessage, Long> {

    List<GpsMessage> findByVehicleIdOrderByIdAsc(String vehicleId);
}
