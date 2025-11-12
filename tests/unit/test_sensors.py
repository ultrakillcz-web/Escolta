"""
Unit tests for sensors
"""

import unittest
from escolta.sensors.camera_sensor import CameraSensor
from escolta.sensors.motion_sensor import MotionSensor


class TestCameraSensor(unittest.TestCase):
    """Test cases for CameraSensor"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.camera = CameraSensor(
            sensor_id="cam-test",
            name="Test Camera",
            location="Test Location"
        )
    
    def test_initialization(self):
        """Test camera sensor initialization"""
        self.assertEqual(self.camera.sensor_id, "cam-test")
        self.assertEqual(self.camera.name, "Test Camera")
        self.assertEqual(self.camera.location, "Test Location")
        self.assertFalse(self.camera.recording)
    
    def test_activate_deactivate(self):
        """Test activating and deactivating camera"""
        self.camera.activate()
        self.assertTrue(self.camera.is_active)
        
        self.camera.deactivate()
        self.assertFalse(self.camera.is_active)
    
    def test_recording(self):
        """Test recording functionality"""
        self.camera.start_recording()
        self.assertTrue(self.camera.recording)
        
        self.camera.stop_recording()
        self.assertFalse(self.camera.recording)
    
    def test_read(self):
        """Test reading camera data"""
        data = self.camera.read()
        
        self.assertEqual(data["sensor_id"], "cam-test")
        self.assertEqual(data["type"], "camera")
        self.assertIn("timestamp", data)


class TestMotionSensor(unittest.TestCase):
    """Test cases for MotionSensor"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.sensor = MotionSensor(
            sensor_id="motion-test",
            name="Test Motion",
            sensitivity=0.5
        )
    
    def test_initialization(self):
        """Test motion sensor initialization"""
        self.assertEqual(self.sensor.sensor_id, "motion-test")
        self.assertEqual(self.sensor.name, "Test Motion")
        self.assertEqual(self.sensor.sensitivity, 0.5)
        self.assertFalse(self.sensor.motion_detected)
    
    def test_trigger_motion(self):
        """Test triggering motion detection"""
        self.sensor.trigger_motion()
        
        self.assertTrue(self.sensor.motion_detected)
        self.assertEqual(self.sensor.detection_count, 1)
    
    def test_reset_motion(self):
        """Test resetting motion detection"""
        self.sensor.trigger_motion()
        self.sensor.reset_motion()
        
        self.assertFalse(self.sensor.motion_detected)
    
    def test_read(self):
        """Test reading motion sensor data"""
        data = self.sensor.read()
        
        self.assertEqual(data["sensor_id"], "motion-test")
        self.assertEqual(data["type"], "motion")
        self.assertIn("timestamp", data)


if __name__ == "__main__":
    unittest.main()
