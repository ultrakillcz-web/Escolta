"""
Tests for alert system module
"""

import json
from escota.core.alert import AlertSystem


class TestAlertSystem:
    """Test AlertSystem class"""

    def test_initialization(self):
        """Test alert system initialization"""
        alert_system = AlertSystem()
        assert alert_system.alerts == []
        assert alert_system.log_file is None

    def test_create_alert(self):
        """Test creating an alert"""
        alert_system = AlertSystem()

        alert = alert_system.create_alert("motion", "Motion detected", {"boxes": 3})

        assert alert["type"] == "motion"
        assert alert["message"] == "Motion detected"
        assert alert["metadata"]["boxes"] == 3
        assert "timestamp" in alert
        assert len(alert_system.alerts) == 1

    def test_get_alerts(self):
        """Test retrieving alerts"""
        alert_system = AlertSystem()

        alert_system.create_alert("motion", "Motion 1")
        alert_system.create_alert("intrusion", "Intrusion 1")
        alert_system.create_alert("motion", "Motion 2")

        # Get all alerts
        all_alerts = alert_system.get_alerts()
        assert len(all_alerts) == 3

        # Get motion alerts only
        motion_alerts = alert_system.get_alerts(alert_type="motion")
        assert len(motion_alerts) == 2
        assert all(a["type"] == "motion" for a in motion_alerts)

        # Get limited alerts
        limited_alerts = alert_system.get_alerts(limit=2)
        assert len(limited_alerts) == 2

    def test_clear_alerts(self):
        """Test clearing alerts"""
        alert_system = AlertSystem()

        alert_system.create_alert("motion", "Test")
        assert len(alert_system.alerts) == 1

        alert_system.clear_alerts()
        assert len(alert_system.alerts) == 0

    def test_save_alert_to_file(self, tmp_path):
        """Test saving alerts to file"""
        log_file = tmp_path / "alerts.log"
        alert_system = AlertSystem(log_file=str(log_file))

        alert_system.create_alert("motion", "Test alert")

        assert log_file.exists()

        # Verify file content
        with open(log_file, "r") as f:
            line = f.readline()
            saved_alert = json.loads(line)
            assert saved_alert["type"] == "motion"
            assert saved_alert["message"] == "Test alert"

    def test_load_alerts_from_file(self, tmp_path):
        """Test loading alerts from file"""
        log_file = tmp_path / "alerts.log"
        alert_system = AlertSystem()

        # Create some alerts in file
        alerts = [
            {
                "timestamp": "2025-01-01T00:00:00",
                "type": "motion",
                "message": "Alert 1",
                "metadata": {},
            },
            {
                "timestamp": "2025-01-01T00:01:00",
                "type": "intrusion",
                "message": "Alert 2",
                "metadata": {},
            },
        ]

        with open(log_file, "w") as f:
            for alert in alerts:
                f.write(json.dumps(alert) + "\n")

        # Load alerts
        loaded_alerts = alert_system.load_alerts_from_file(str(log_file))
        assert len(loaded_alerts) == 2
        assert loaded_alerts[0]["type"] == "motion"
        assert loaded_alerts[1]["type"] == "intrusion"
