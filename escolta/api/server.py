"""
API server for the security system
"""

import logging
from typing import Dict, Any


logger = logging.getLogger(__name__)


class SecurityAPI:
    """
    RESTful API server for the security system
    """
    
    def __init__(self, security_monitor, alert_manager, config_manager):
        """
        Initialize the API server
        
        Args:
            security_monitor: SecurityMonitor instance
            alert_manager: AlertManager instance
            config_manager: ConfigManager instance
        """
        self.security_monitor = security_monitor
        self.alert_manager = alert_manager
        self.config_manager = config_manager
        self.host = "0.0.0.0"
        self.port = 8080
        logger.info("SecurityAPI initialized")
    
    def start(self):
        """Start the API server"""
        logger.info(f"API server starting on {self.host}:{self.port}")
        # In a real implementation, this would start a web server
        # For now, we just log the action
        return True
    
    def stop(self):
        """Stop the API server"""
        logger.info("API server stopping")
        return True
    
    def get_system_status(self) -> Dict[str, Any]:
        """
        Get the overall system status
        
        Returns:
            Dictionary with system status
        """
        return {
            "security_monitor": self.security_monitor.get_status(),
            "active_alerts": len(self.alert_manager.get_active_alerts()),
            "config": {
                "name": self.config_manager.get("system.name"),
                "version": self.config_manager.get("system.version")
            }
        }
    
    def get_sensors(self) -> Dict[str, Any]:
        """
        Get all sensors
        
        Returns:
            Dictionary with sensor information
        """
        sensors = []
        for sensor in self.security_monitor.sensors:
            sensors.append(sensor.get_status())
        
        return {
            "count": len(sensors),
            "sensors": sensors
        }
    
    def get_alerts(self, severity: str = None) -> Dict[str, Any]:
        """
        Get alerts, optionally filtered by severity
        
        Args:
            severity: Optional severity filter
            
        Returns:
            Dictionary with alerts
        """
        alerts = self.alert_manager.get_active_alerts(severity)
        
        return {
            "count": len(alerts),
            "alerts": alerts
        }
