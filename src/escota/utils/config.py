"""
Configuration management utilities
"""

import yaml
from pathlib import Path
from typing import Dict, Any


def load_config(config_path: str) -> Dict[str, Any]:
    """
    Load configuration from YAML file

    Args:
        config_path: Path to configuration file

    Returns:
        Configuration dictionary
    """
    try:
        with open(config_path, "r") as f:
            return yaml.safe_load(f) or {}
    except FileNotFoundError:
        print(f"Config file not found: {config_path}")
        return {}
    except yaml.YAMLError as e:
        print(f"Error parsing config file: {e}")
        return {}


def save_config(config: Dict[str, Any], config_path: str):
    """
    Save configuration to YAML file

    Args:
        config: Configuration dictionary
        config_path: Path to save configuration
    """
    try:
        config_file = Path(config_path)
        config_file.parent.mkdir(parents=True, exist_ok=True)

        with open(config_path, "w") as f:
            yaml.dump(config, f, default_flow_style=False)
    except Exception as e:
        print(f"Error saving config: {e}")


def get_default_config() -> Dict[str, Any]:
    """
    Get default configuration

    Returns:
        Default configuration dictionary
    """
    return {
        "camera": {"id": 0, "resolution": [640, 480], "fps": 30},
        "detection": {"threshold": 25, "min_area": 500, "enabled": True},
        "alerts": {"log_file": "logs/alerts.log", "enabled": True},
        "recording": {"enabled": False, "output_dir": "recordings", "format": "mp4"},
        "database": {"enabled": False, "db_path": "escota_alerts.db"},
        "email": {
            "enabled": False,
            "smtp_server": "smtp.gmail.com",
            "smtp_port": 587,
            "sender_email": "",
            "sender_password": "",
            "recipients": [],
        },
        "webui": {"enabled": False, "host": "localhost", "port": 8080},
    }
