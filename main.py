#!/usr/bin/env python3
"""
Main entry point for the Escolta security system
"""

import argparse
from escolta.core.security_monitor import SecurityMonitor
from escolta.alerts.alert_manager import AlertManager
from escolta.config.config_manager import ConfigManager
from escolta.api.server import SecurityAPI
from escolta.sensors.camera_sensor import CameraSensor
from escolta.sensors.motion_sensor import MotionSensor
from escolta.utils.logger import setup_logger


def main():
    """Main function to run the Escolta security system"""
    parser = argparse.ArgumentParser(
        description="Escolta - Sistema de Segurança Privada Inteligente"
    )
    parser.add_argument(
        "--config",
        type=str,
        help="Path to configuration file"
    )
    parser.add_argument(
        "--log-level",
        type=str,
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        help="Logging level"
    )
    
    args = parser.parse_args()
    
    # Setup logging
    logger = setup_logger(level=args.log_level)
    logger.info("Starting Escolta Security System")
    
    # Initialize components
    config_manager = ConfigManager(args.config)
    security_monitor = SecurityMonitor(config_manager.config)
    alert_manager = AlertManager()
    api = SecurityAPI(security_monitor, alert_manager, config_manager)
    
    # Example: Add some sensors
    camera1 = CameraSensor(
        sensor_id="cam-001",
        name="Front Door Camera",
        location="Entrance",
        resolution="1080p"
    )
    
    motion1 = MotionSensor(
        sensor_id="motion-001",
        name="Living Room Motion",
        location="Living Room",
        sensitivity=0.7
    )
    
    security_monitor.add_sensor(camera1)
    security_monitor.add_sensor(motion1)
    
    # Activate sensors
    camera1.activate()
    motion1.activate()
    
    # Start monitoring
    security_monitor.start()
    
    logger.info("Escolta Security System is running")
    logger.info(f"System status: {security_monitor.get_status()}")
    
    # In a real application, this would run continuously
    # For now, we just demonstrate the system initialization
    
    return 0


if __name__ == "__main__":
    exit(main())
