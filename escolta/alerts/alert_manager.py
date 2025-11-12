"""
Alert management system
"""

import logging
from typing import Dict, Any, List
from datetime import datetime


logger = logging.getLogger(__name__)


class AlertManager:
    """
    Manages security alerts and notifications
    """
    
    def __init__(self):
        """Initialize the alert manager"""
        self.alerts = []
        self.alert_handlers = []
        logger.info("AlertManager initialized")
    
    def create_alert(self, severity: str, message: str, source: str = "", 
                     metadata: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Create a new security alert
        
        Args:
            severity: Alert severity level (low, medium, high, critical)
            message: Alert message
            source: Source of the alert
            metadata: Additional alert metadata
            
        Returns:
            Dictionary containing the created alert
        """
        alert = {
            "id": len(self.alerts) + 1,
            "severity": severity,
            "message": message,
            "source": source,
            "metadata": metadata or {},
            "timestamp": datetime.now().isoformat(),
            "acknowledged": False
        }
        
        self.alerts.append(alert)
        logger.warning(f"Alert created: {severity} - {message}")
        
        # Notify all registered handlers
        for handler in self.alert_handlers:
            try:
                handler(alert)
            except Exception as e:
                logger.error(f"Error in alert handler: {e}")
        
        return alert
    
    def acknowledge_alert(self, alert_id: int):
        """
        Acknowledge an alert
        
        Args:
            alert_id: ID of the alert to acknowledge
        """
        for alert in self.alerts:
            if alert["id"] == alert_id:
                alert["acknowledged"] = True
                alert["acknowledged_at"] = datetime.now().isoformat()
                logger.info(f"Alert {alert_id} acknowledged")
                return True
        return False
    
    def get_active_alerts(self, severity: str = None) -> List[Dict[str, Any]]:
        """
        Get all active (unacknowledged) alerts
        
        Args:
            severity: Optional severity filter
            
        Returns:
            List of active alerts
        """
        active = [a for a in self.alerts if not a["acknowledged"]]
        if severity:
            active = [a for a in active if a["severity"] == severity]
        return active
    
    def register_handler(self, handler):
        """
        Register an alert handler function
        
        Args:
            handler: Function to call when alerts are created
        """
        self.alert_handlers.append(handler)
        logger.info("Alert handler registered")
