#!/usr/bin/env python
"""
Configuration Management Example

This example demonstrates how to work with configuration files.
"""

from escota.utils.config import get_default_config, save_config, load_config
import yaml


def main():
    print("Escota Configuration Management Example")
    print("=" * 50)

    # Get default configuration
    print("\n1. Default Configuration:")
    print("-" * 50)
    config = get_default_config()
    print(yaml.dump(config, default_flow_style=False))

    # Modify configuration
    print("\n2. Modified Configuration:")
    print("-" * 50)
    config["camera"]["resolution"] = [1920, 1080]
    config["detection"]["threshold"] = 30
    config["detection"]["min_area"] = 1000
    config["alerts"]["enabled"] = True

    print(yaml.dump(config, default_flow_style=False))

    # Save configuration
    config_path = "config/custom_config.yaml"
    print(f"\n3. Saving configuration to: {config_path}")
    save_config(config, config_path)
    print("Configuration saved successfully!")

    # Load configuration
    print(f"\n4. Loading configuration from: {config_path}")
    loaded_config = load_config(config_path)

    print("\nLoaded configuration:")
    print(yaml.dump(loaded_config, default_flow_style=False))

    # Verify configuration values
    print("\n5. Configuration Values:")
    print("-" * 50)
    print(f"Camera Resolution: {loaded_config['camera']['resolution']}")
    print(f"Detection Threshold: {loaded_config['detection']['threshold']}")
    print(f"Detection Min Area: {loaded_config['detection']['min_area']}")
    print(f"Alerts Enabled: {loaded_config['alerts']['enabled']}")

    print("\n✅ Configuration management example completed!")


if __name__ == "__main__":
    main()
