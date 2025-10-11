"""
Escolta - Sistema de Segurança Privada Inteligente
Intelligent Private Security System
"""

__version__ = "0.1.0"
__author__ = "Escolta Team"

from escolta.core.security_monitor import SecurityMonitor
from escolta.core.event_handler import EventHandler

__all__ = ["SecurityMonitor", "EventHandler"]
