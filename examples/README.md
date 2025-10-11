# Escota Examples

This directory contains example scripts demonstrating how to use the Escota security system.

## Available Examples

### 1. Alert System Example (`alert_example.py`)

Demonstrates the alert system functionality without requiring camera hardware.

**Features:**
- Creating alerts with different types and metadata
- Filtering alerts by type
- Getting latest alerts
- Logging alerts to file

**Run:**
```bash
python alert_example.py
```

### 2. Configuration Management Example (`config_example.py`)

Shows how to work with YAML configuration files.

**Features:**
- Loading default configuration
- Modifying configuration values
- Saving configuration to file
- Loading configuration from file

**Run:**
```bash
python config_example.py
```

## Camera Examples (Requires OpenCV)

To run camera and motion detection examples, install OpenCV:

```bash
pip install opencv-python numpy
```

Then you can create your own examples based on the README documentation.

## Creating Your Own Examples

1. Import the necessary modules from `escota`
2. Configure components as needed
3. Run your security logic
4. Handle alerts and logging

Example template:

```python
from escota.core.alert import AlertSystem
from escota.utils.config import load_config

# Initialize
config = load_config('config/escota.yaml')
alert_system = AlertSystem(log_file='logs/my_alerts.log')

# Your security logic here
# ...

# Create alerts
alert_system.create_alert('motion', 'Custom alert message')
```

## Environment Setup

Ensure the package is installed or add to PYTHONPATH:

```bash
# Install in development mode
pip install -e .

# Or set PYTHONPATH
export PYTHONPATH=/path/to/Escota/src:$PYTHONPATH
```
