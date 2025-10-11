"""
Alert system module for security notifications
"""

import json
from datetime import datetime
from typing import Dict, List, Optional
from pathlib import Path


class AlertSystem:
    """System for managing security alerts"""

    def __init__(self, log_file: Optional[str] = None):
        """
        Initialize alert system

        Args:
            log_file: Path to alert log file (optional)
        """
        self.log_file = log_file
        self.alerts: List[Dict] = []

    def create_alert(self, alert_type: str, message: str, metadata: Optional[Dict] = None) -> Dict:
        """
        Create a new alert

        Args:
            alert_type: Type of alert (e.g., 'motion', 'intrusion')
            message: Alert message
            metadata: Additional metadata

        Returns:
            Alert dictionary
        """
        alert = {
            "timestamp": datetime.now().isoformat(),
            "type": alert_type,
            "message": message,
            "metadata": metadata or {},
        }

        self.alerts.append(alert)

        # Save to log file if configured
        if self.log_file:
            self._save_alert(alert)

        return alert

    def get_alerts(
        self, alert_type: Optional[str] = None, limit: Optional[int] = None
    ) -> List[Dict]:
        """
        Get alerts, optionally filtered by type

        Args:
            alert_type: Filter by alert type (optional)
            limit: Maximum number of alerts to return (optional)

        Returns:
            List of alerts
        """
        alerts = self.alerts

        if alert_type:
            alerts = [a for a in alerts if a["type"] == alert_type]

        if limit:
            alerts = alerts[-limit:]

        return alerts

    def clear_alerts(self):
        """Clear all alerts"""
        self.alerts = []

    def _save_alert(self, alert: Dict):
        """Save alert to log file"""
        try:
            log_path = Path(self.log_file)
            log_path.parent.mkdir(parents=True, exist_ok=True)

            with open(self.log_file, "a") as f:
                f.write(json.dumps(alert) + "\n")
        except Exception as e:
            print(f"Error saving alert: {e}")

    def load_alerts_from_file(self, filepath: str) -> List[Dict]:
        """
        Load alerts from log file

        Args:
            filepath: Path to log file

        Returns:
            List of alerts
        """
        alerts = []
        try:
            with open(filepath, "r") as f:
                for line in f:
                    if line.strip():
                        alerts.append(json.loads(line))
        except Exception as e:
            print(f"Error loading alerts: {e}")

        return alerts
