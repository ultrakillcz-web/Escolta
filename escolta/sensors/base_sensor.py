"""
Base sensor class for all security sensors
"""

import logging
from abc import ABC, abstractmethod
from typing import Dict, Any
from datetime import datetime


logger = logging.getLogger(__name__)


class BaseSensor(ABC):
    """
    Abstract base class for all sensors
    """
    
    def __init__(self, sensor_id: str, name: str, location: str = ""):
        """
        Initialize a sensor
        
        Args:
            sensor_id: Unique identifier for the sensor
            name: Human-readable name for the sensor
            location: Physical location of the sensor
        """
        self.sensor_id = sensor_id
        self.name = name
        self.location = location
        self.is_active = False
        self.last_reading = None
        logger.info(f"Sensor initialized: {name} ({sensor_id})")
    
    def activate(self):
        """Activate the sensor"""
        self.is_active = True
        logger.info(f"Sensor activated: {self.name}")
    
    def deactivate(self):
        """Deactivate the sensor"""
        self.is_active = False
        logger.info(f"Sensor deactivated: {self.name}")
    
    @abstractmethod
    def read(self) -> Dict[str, Any]:
        """
        Read data from the sensor
        
        Returns:
            Dictionary containing sensor reading data
        """
        pass
    
    def get_status(self) -> Dict[str, Any]:
        """
        Get the current status of the sensor
        
        Returns:
            Dictionary with sensor status information
        """
        return {
            "sensor_id": self.sensor_id,
            "name": self.name,
            "location": self.location,
            "active": self.is_active,
            "last_reading": self.last_reading,
            "timestamp": datetime.now().isoformat()
        }
