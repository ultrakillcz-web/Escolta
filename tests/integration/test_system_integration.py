"""
Integration test for the complete security system
"""

import unittest
from escolta.core.security_monitor import SecurityMonitor
from escolta.sensors.camera_sensor import CameraSensor
from escolta.sensors.motion_sensor import MotionSensor
from escolta.alerts.alert_manager import AlertManager
from escolta.alerts.notification import Notification
from escolta.config.config_manager import ConfigManager


class TestSecuritySystemIntegration(unittest.TestCase):
    """Integration tests for the complete security system"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.config_manager = ConfigManager()
        self.monitor = SecurityMonitor(self.config_manager.config)
        self.alert_manager = AlertManager()
        self.notification = Notification()
    
    def test_complete_workflow(self):
        """Test a complete security monitoring workflow"""
        # Create and add sensors
        camera = CameraSensor(
            sensor_id="cam-001",
            name="Test Camera",
            location="Entrance"
        )
        
        motion = MotionSensor(
            sensor_id="motion-001",
            name="Test Motion",
            location="Living Room"
        )
        
        self.monitor.add_sensor(camera)
        self.monitor.add_sensor(motion)
        
        # Activate sensors
        camera.activate()
        motion.activate()
        
        # Start monitoring
        self.assertTrue(self.monitor.start())
        self.assertTrue(self.monitor.is_active)
        
        # Simulate motion detection
        motion.trigger_motion()
        self.assertTrue(motion.motion_detected)
        
        # Record the event
        event = {
            "type": "motion_detected",
            "sensor_id": motion.sensor_id,
            "location": motion.location
        }
        self.monitor.record_event(event)
        
        # Create an alert
        alert = self.alert_manager.create_alert(
            severity="high",
            message=f"Motion detected at {motion.location}",
            source=motion.sensor_id
        )
        
        self.assertEqual(alert["severity"], "high")
        self.assertFalse(alert["acknowledged"])
        
        # Add notification recipient
        self.notification.add_recipient("push", "test-device-001")
        
        # Send notification
        result = self.notification.send_notification(
            channel="push",
            message="Motion detected!",
            alert_data=alert
        )
        self.assertTrue(result)
        
        # Acknowledge the alert
        self.alert_manager.acknowledge_alert(alert["id"])
        
        # Get active alerts (should be empty now)
        active_alerts = self.alert_manager.get_active_alerts()
        self.assertEqual(len(active_alerts), 0)
        
        # Check system status
        status = self.monitor.get_status()
        self.assertTrue(status["active"])
        self.assertEqual(status["sensors_count"], 2)
        self.assertEqual(status["events_count"], 1)
        
        # Stop monitoring
        self.assertTrue(self.monitor.stop())
        self.assertFalse(self.monitor.is_active)


if __name__ == "__main__":
    unittest.main()
