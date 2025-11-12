"""
Main security monitoring system
"""

import logging
from typing import List, Dict, Any
from datetime import datetime


logger = logging.getLogger(__name__)


class SecurityMonitor:
    """
    Main security monitoring class that coordinates sensors, alerts, and event handling
    """
    
    def __init__(self, config: Dict[str, Any] = None):
        """
        Initialize the security monitor
        
        Args:
            config: Configuration dictionary for the security system
        """
        self.config = config or {}
        self.sensors = []
        self.is_active = False
        self.events = []
        logger.info("SecurityMonitor initialized")
    
    def start(self):
        """Start the security monitoring system"""
        self.is_active = True
        logger.info("Security monitoring started")
        return True
    
    def stop(self):
        """Stop the security monitoring system"""
        self.is_active = False
        logger.info("Security monitoring stopped")
        return True
    
    def add_sensor(self, sensor):
        """
        Add a sensor to the monitoring system
        
        Args:
            sensor: Sensor object to add
        """
        self.sensors.append(sensor)
        logger.info(f"Sensor added: {sensor}")
    
    def remove_sensor(self, sensor):
        """
        Remove a sensor from the monitoring system
        
        Args:
            sensor: Sensor object to remove
        """
        if sensor in self.sensors:
            self.sensors.remove(sensor)
            logger.info(f"Sensor removed: {sensor}")
    
    def get_status(self) -> Dict[str, Any]:
        """
        Get the current status of the security system
        
        Returns:
            Dictionary with system status information
        """
        return {
            "active": self.is_active,
            "sensors_count": len(self.sensors),
            "events_count": len(self.events),
            "timestamp": datetime.now().isoformat()
        }
    
    def record_event(self, event: Dict[str, Any]):
        """
        Record a security event
        
        Args:
            event: Event dictionary containing event information
        """
        event["timestamp"] = datetime.now().isoformat()
        self.events.append(event)
        logger.warning(f"Security event recorded: {event.get('type', 'unknown')}")
