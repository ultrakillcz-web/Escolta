"""
Escota - Sistema de Segurança privada inteligente
Intelligent Private Security System
"""

__version__ = "0.1.0"
__author__ = "Leonardo Morais"
__license__ = "LGPL-2.1"

from escota.core.camera import CameraMonitor
from escota.core.detector import MotionDetector
from escota.core.alert import AlertSystem

__all__ = [
    "CameraMonitor",
    "MotionDetector",
    "AlertSystem",
]
