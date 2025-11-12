"""
Database models for the security system
"""

import logging
from datetime import datetime
from typing import Dict, Any, List


logger = logging.getLogger(__name__)


class Event:
    """
    Represents a security event
    """
    
    def __init__(self, event_type: str, source: str, data: Dict[str, Any] = None):
        """
        Initialize an event
        
        Args:
            event_type: Type of event
            source: Source of the event
            data: Event data
        """
        self.id = None
        self.event_type = event_type
        self.source = source
        self.data = data or {}
        self.timestamp = datetime.now()
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert event to dictionary"""
        return {
            "id": self.id,
            "type": self.event_type,
            "source": self.source,
            "data": self.data,
            "timestamp": self.timestamp.isoformat()
        }


class Sensor:
    """
    Represents a sensor in the database
    """
    
    def __init__(self, sensor_id: str, name: str, sensor_type: str, 
                 location: str = "", config: Dict[str, Any] = None):
        """
        Initialize a sensor record
        
        Args:
            sensor_id: Unique sensor identifier
            name: Sensor name
            sensor_type: Type of sensor
            location: Physical location
            config: Sensor configuration
        """
        self.id = None
        self.sensor_id = sensor_id
        self.name = name
        self.sensor_type = sensor_type
        self.location = location
        self.config = config or {}
        self.active = False
        self.created_at = datetime.now()
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert sensor to dictionary"""
        return {
            "id": self.id,
            "sensor_id": self.sensor_id,
            "name": self.name,
            "type": self.sensor_type,
            "location": self.location,
            "config": self.config,
            "active": self.active,
            "created_at": self.created_at.isoformat()
        }


class Alert:
    """
    Represents a security alert
    """
    
    def __init__(self, severity: str, message: str, source: str = "", 
                 metadata: Dict[str, Any] = None):
        """
        Initialize an alert
        
        Args:
            severity: Alert severity
            message: Alert message
            source: Alert source
            metadata: Additional metadata
        """
        self.id = None
        self.severity = severity
        self.message = message
        self.source = source
        self.metadata = metadata or {}
        self.acknowledged = False
        self.timestamp = datetime.now()
        self.acknowledged_at = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert alert to dictionary"""
        return {
            "id": self.id,
            "severity": self.severity,
            "message": self.message,
            "source": self.source,
            "metadata": self.metadata,
            "acknowledged": self.acknowledged,
            "timestamp": self.timestamp.isoformat(),
            "acknowledged_at": self.acknowledged_at.isoformat() if self.acknowledged_at else None
        }
