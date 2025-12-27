"""
Escota - Sistema de Segurança privada inteligente
Intelligent Private Security System
"""

__version__ = "0.2.0"
__author__ = "Leonardo Morais"
__license__ = "LGPL-2.1"

from escota.core.camera import CameraMonitor
from escota.core.detector import MotionDetector
from escota.core.alert import AlertSystem
from escota.core.notifier import EmailNotifier
from escota.core.database import AlertDatabase
from escota.core.webui import WebInterface

__all__ = [
    "CameraMonitor",
    "MotionDetector",
    "AlertSystem",
    "EmailNotifier",
    "AlertDatabase",
    "WebInterface",
]
