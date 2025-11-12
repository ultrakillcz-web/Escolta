"""
Motion sensor for detecting movement
"""

import logging
from typing import Dict, Any
from datetime import datetime
from escolta.sensors.base_sensor import BaseSensor


logger = logging.getLogger(__name__)


class MotionSensor(BaseSensor):
    """
    Motion sensor for detecting movement
    """
    
    def __init__(self, sensor_id: str, name: str, location: str = "", 
                 sensitivity: float = 0.5):
        """
        Initialize a motion sensor
        
        Args:
            sensor_id: Unique identifier for the sensor
            name: Human-readable name for the sensor
            location: Physical location of the sensor
            sensitivity: Detection sensitivity (0.0 to 1.0)
        """
        super().__init__(sensor_id, name, location)
        self.sensitivity = max(0.0, min(1.0, sensitivity))
        self.motion_detected = False
        self.detection_count = 0
    
    def read(self) -> Dict[str, Any]:
        """
        Read data from the motion sensor
        
        Returns:
            Dictionary containing motion sensor data
        """
        reading = {
            "sensor_id": self.sensor_id,
            "type": "motion",
            "timestamp": datetime.now().isoformat(),
            "motion_detected": self.motion_detected,
            "sensitivity": self.sensitivity,
            "detection_count": self.detection_count,
            "active": self.is_active
        }
        self.last_reading = reading
        return reading
    
    def trigger_motion(self):
        """Trigger a motion detection event"""
        self.motion_detected = True
        self.detection_count += 1
        logger.warning(f"Motion detected by {self.name} at {self.location}")
    
    def reset_motion(self):
        """Reset motion detection state"""
        self.motion_detected = False
