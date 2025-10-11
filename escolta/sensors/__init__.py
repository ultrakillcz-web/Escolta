"""
Sensor modules for the security system
"""

from escolta.sensors.base_sensor import BaseSensor
from escolta.sensors.camera_sensor import CameraSensor
from escolta.sensors.motion_sensor import MotionSensor

__all__ = ["BaseSensor", "CameraSensor", "MotionSensor"]
