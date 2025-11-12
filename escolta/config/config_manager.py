"""
Configuration management for the security system
"""

import json
import logging
from typing import Dict, Any
from pathlib import Path


logger = logging.getLogger(__name__)


class ConfigManager:
    """
    Manages system configuration
    """
    
    def __init__(self, config_file: str = None):
        """
        Initialize configuration manager
        
        Args:
            config_file: Path to configuration file
        """
        self.config_file = config_file
        self.config = self._load_default_config()
        
        if config_file and Path(config_file).exists():
            self.load_config(config_file)
        
        logger.info("ConfigManager initialized")
    
    def _load_default_config(self) -> Dict[str, Any]:
        """
        Load default configuration
        
        Returns:
            Default configuration dictionary
        """
        return {
            "system": {
                "name": "Escolta Security System",
                "version": "0.1.0",
                "log_level": "INFO"
            },
            "sensors": {
                "scan_interval": 5,
                "auto_activate": True
            },
            "alerts": {
                "enabled": True,
                "default_severity": "medium"
            },
            "notifications": {
                "email_enabled": False,
                "sms_enabled": False,
                "push_enabled": True
            },
            "database": {
                "type": "sqlite",
                "path": "escolta.db"
            }
        }
    
    def load_config(self, config_file: str) -> bool:
        """
        Load configuration from file
        
        Args:
            config_file: Path to configuration file
            
        Returns:
            True if configuration was loaded successfully
        """
        try:
            with open(config_file, 'r') as f:
                loaded_config = json.load(f)
                self.config.update(loaded_config)
                logger.info(f"Configuration loaded from {config_file}")
                return True
        except Exception as e:
            logger.error(f"Error loading configuration: {e}")
            return False
    
    def save_config(self, config_file: str = None) -> bool:
        """
        Save configuration to file
        
        Args:
            config_file: Path to configuration file (uses default if not provided)
            
        Returns:
            True if configuration was saved successfully
        """
        file_path = config_file or self.config_file
        if not file_path:
            logger.error("No configuration file specified")
            return False
        
        try:
            with open(file_path, 'w') as f:
                json.dump(self.config, f, indent=2)
                logger.info(f"Configuration saved to {file_path}")
                return True
        except Exception as e:
            logger.error(f"Error saving configuration: {e}")
            return False
    
    def get(self, key: str, default: Any = None) -> Any:
        """
        Get a configuration value
        
        Args:
            key: Configuration key (supports dot notation, e.g., 'system.name')
            default: Default value if key doesn't exist
            
        Returns:
            Configuration value or default
        """
        keys = key.split('.')
        value = self.config
        
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        
        return value
    
    def set(self, key: str, value: Any):
        """
        Set a configuration value
        
        Args:
            key: Configuration key (supports dot notation)
            value: Value to set
        """
        keys = key.split('.')
        config = self.config
        
        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]
        
        config[keys[-1]] = value
        logger.info(f"Configuration updated: {key} = {value}")
