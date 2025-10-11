"""
Unit tests for SecurityMonitor
"""

import unittest
from escolta.core.security_monitor import SecurityMonitor
from escolta.sensors.motion_sensor import MotionSensor


class TestSecurityMonitor(unittest.TestCase):
    """Test cases for SecurityMonitor"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.monitor = SecurityMonitor()
    
    def test_initialization(self):
        """Test SecurityMonitor initialization"""
        self.assertIsNotNone(self.monitor)
        self.assertEqual(len(self.monitor.sensors), 0)
        self.assertFalse(self.monitor.is_active)
    
    def test_start_stop(self):
        """Test starting and stopping the monitor"""
        self.assertTrue(self.monitor.start())
        self.assertTrue(self.monitor.is_active)
        
        self.assertTrue(self.monitor.stop())
        self.assertFalse(self.monitor.is_active)
    
    def test_add_sensor(self):
        """Test adding a sensor"""
        sensor = MotionSensor("test-001", "Test Sensor")
        self.monitor.add_sensor(sensor)
        
        self.assertEqual(len(self.monitor.sensors), 1)
        self.assertIn(sensor, self.monitor.sensors)
    
    def test_remove_sensor(self):
        """Test removing a sensor"""
        sensor = MotionSensor("test-001", "Test Sensor")
        self.monitor.add_sensor(sensor)
        self.monitor.remove_sensor(sensor)
        
        self.assertEqual(len(self.monitor.sensors), 0)
        self.assertNotIn(sensor, self.monitor.sensors)
    
    def test_get_status(self):
        """Test getting system status"""
        status = self.monitor.get_status()
        
        self.assertIn("active", status)
        self.assertIn("sensors_count", status)
        self.assertIn("events_count", status)
        self.assertIn("timestamp", status)
    
    def test_record_event(self):
        """Test recording an event"""
        event = {"type": "test", "data": "test data"}
        self.monitor.record_event(event)
        
        self.assertEqual(len(self.monitor.events), 1)
        self.assertIn("timestamp", self.monitor.events[0])


if __name__ == "__main__":
    unittest.main()
