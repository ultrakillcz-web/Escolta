# Escota

![CI](https://github.com/ultrakillcz-web/Escota/workflows/CI/badge.svg)
[![License: LGPL v2.1](https://img.shields.io/badge/License-LGPL%20v2.1-blue.svg)](https://www.gnu.org/licenses/lgpl-2.1)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

**Sistema de Segurança privada inteligente** (Intelligent Private Security System)

Escota is a Python-based intelligent security monitoring system that provides real-time motion detection, alert management, and video surveillance capabilities.

## Features

- 📹 **Camera Monitoring**: Real-time video capture from webcams or IP cameras
- 🔍 **Motion Detection**: Intelligent motion detection with configurable sensitivity
- 🚨 **Alert System**: Comprehensive alert logging and notification system
- ⚙️ **Configurable**: YAML-based configuration for easy customization
- 🧪 **Well-Tested**: Comprehensive test suite with pytest
- 🐍 **Modern Python**: Built with Python 3.8+ using type hints

## Installation

### Quick Install

```bash
pip install -e .
```

For full camera and motion detection features:

```bash
pip install opencv-python numpy
```

See [INSTALLATION.md](docs/INSTALLATION.md) for detailed installation instructions.

## Quick Start

### 1. Initialize Configuration

```bash
escota config init
```

This creates a default configuration file at `config/escota.yaml`.

### 2. View Configuration

```bash
escota config show
```

### 3. Start Monitoring

```bash
escota monitor --config config/escota.yaml
```

## Configuration

The configuration file (`config/escota.yaml`) allows you to customize:

```yaml
camera:
  id: 0                # Camera device ID (0 for default)
  resolution:
    - 640
    - 480
  fps: 30

detection:
  threshold: 25        # Motion detection threshold (0-255)
  min_area: 500       # Minimum area for motion detection
  enabled: true

alerts:
  log_file: logs/alerts.log
  enabled: true

recording:
  enabled: false
  output_dir: recordings
  format: mp4
```

## Usage Examples

### Command Line

```bash
# Initialize default configuration
escota config init

# View configuration
escota config show

# Start monitoring with custom config
escota monitor --config my_config.yaml

# Process limited number of frames (useful for testing)
escota monitor --max-frames 100
```

### Python API

#### Alert System Example

```python
from escota.core.alert import AlertSystem

# Initialize alert system with log file
alert_system = AlertSystem(log_file="logs/alerts.log")

# Create an alert
alert_system.create_alert(
    'motion',
    'Motion detected in Zone A',
    {'zone': 'A', 'confidence': 0.95}
)

# Get all alerts
all_alerts = alert_system.get_alerts()

# Get motion alerts only
motion_alerts = alert_system.get_alerts(alert_type='motion')

# Get latest 10 alerts
recent_alerts = alert_system.get_alerts(limit=10)
```

#### Configuration Example

```python
from escota.utils.config import load_config, save_config, get_default_config

# Get default configuration
config = get_default_config()

# Modify configuration
config['camera']['resolution'] = [1920, 1080]
config['detection']['threshold'] = 30

# Save configuration
save_config(config, 'config/my_config.yaml')

# Load configuration
loaded_config = load_config('config/my_config.yaml')
```

#### Camera and Motion Detection (requires OpenCV)

```python
from escota.core.camera import CameraMonitor
from escota.core.detector import MotionDetector
from escota.core.alert import AlertSystem

# Initialize components
camera = CameraMonitor(camera_id=0, resolution=(640, 480))
detector = MotionDetector(threshold=25, min_area=500)
alerts = AlertSystem(log_file="logs/alerts.log")

# Start monitoring
with camera:
    while True:
        frame = camera.get_frame()
        if frame is None:
            break
        
        motion_detected, boxes = detector.detect(frame)
        
        if motion_detected:
            alerts.create_alert(
                'motion',
                f'Motion detected: {len(boxes)} regions',
                {'boxes': boxes}
            )
```

### Example Scripts

See the `examples/` directory for complete working examples:

- `alert_example.py` - Alert system demonstration
- `config_example.py` - Configuration management

Run examples:
```bash
python examples/alert_example.py
python examples/config_example.py
```

## Development

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=escota --cov-report=term-missing

# Run specific test file
pytest tests/test_camera.py -v
```

### Code Quality

```bash
# Format code with black
black src tests

# Lint with flake8
flake8 src tests

# Type checking with mypy
mypy src --ignore-missing-imports
```

### Building

```bash
# Build distribution packages
python -m build

# Install locally
pip install -e .
```

## Project Structure

```
Escota/
├── src/escota/          # Main package
│   ├── core/           # Core modules
│   │   ├── camera.py   # Camera monitoring
│   │   ├── detector.py # Motion detection
│   │   └── alert.py    # Alert system
│   ├── utils/          # Utilities
│   │   └── config.py   # Configuration management
│   └── cli.py          # Command-line interface
├── tests/              # Test suite
├── config/             # Configuration files
├── docs/               # Documentation
└── .github/workflows/  # CI/CD pipelines
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history and changes.

## License

This project is licensed under the GNU Lesser General Public License v2.1 - see the [LICENSE](LICENSE) file for details.

## Authors

- **Leonardo Morais** - *Initial work* - [ultrakillcz-web](https://github.com/ultrakillcz-web)

## Acknowledgments

- Built with OpenCV for computer vision capabilities
- Uses PyYAML for configuration management
- Tested with pytest framework
