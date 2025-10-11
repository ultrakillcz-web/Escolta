"""
Tests for configuration utilities
"""

import pytest
from pathlib import Path
from escota.utils.config import load_config, save_config, get_default_config


class TestConfig:
    """Test configuration utilities"""

    def test_get_default_config(self):
        """Test getting default configuration"""
        config = get_default_config()

        assert "camera" in config
        assert "detection" in config
        assert "alerts" in config
        assert "recording" in config

        assert config["camera"]["id"] == 0
        assert config["detection"]["threshold"] == 25

    def test_save_and_load_config(self, tmp_path):
        """Test saving and loading configuration"""
        config_file = tmp_path / "test_config.yaml"

        test_config = {
            "camera": {"id": 1, "resolution": [1920, 1080]},
            "detection": {"threshold": 30},
        }

        # Save config
        save_config(test_config, str(config_file))
        assert config_file.exists()

        # Load config
        loaded_config = load_config(str(config_file))
        assert loaded_config == test_config

    def test_load_nonexistent_config(self):
        """Test loading nonexistent configuration file"""
        config = load_config("/nonexistent/config.yaml")
        assert config == {}

    def test_save_config_creates_directory(self, tmp_path):
        """Test that save_config creates parent directories"""
        config_file = tmp_path / "subdir" / "config.yaml"

        save_config({"test": "value"}, str(config_file))

        assert config_file.exists()
        assert config_file.parent.exists()
