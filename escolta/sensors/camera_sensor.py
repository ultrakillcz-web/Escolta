"""
Camera sensor for video surveillance
"""

import logging
from typing import Dict, Any
from datetime import datetime
from escolta.sensors.base_sensor import BaseSensor


logger = logging.getLogger(__name__)


class CameraSensor(BaseSensor):
    """
    Camera sensor for video surveillance
    """
    
    def __init__(self, sensor_id: str, name: str, location: str = "", 
                 camera_url: str = "", resolution: str = "1080p"):
        """
        Initialize a camera sensor
        
        Args:
            sensor_id: Unique identifier for the sensor
            name: Human-readable name for the sensor
            location: Physical location of the sensor
            camera_url: URL or path to camera feed
            resolution: Video resolution
        """
        super().__init__(sensor_id, name, location)
        self.camera_url = camera_url
        self.resolution = resolution
        self.recording = False
    
    def read(self) -> Dict[str, Any]:
        """
        Read data from the camera
        
        Returns:
            Dictionary containing camera data
        """
        reading = {
            "sensor_id": self.sensor_id,
            "type": "camera",
            "timestamp": datetime.now().isoformat(),
            "camera_url": self.camera_url,
            "resolution": self.resolution,
            "recording": self.recording,
            "active": self.is_active
        }
        self.last_reading = reading
        return reading
    
    def start_recording(self):
        """Start video recording"""
        self.recording = True
        logger.info(f"Camera {self.name} started recording")
    
    def stop_recording(self):
        """Stop video recording"""
        self.recording = False
        logger.info(f"Camera {self.name} stopped recording")
