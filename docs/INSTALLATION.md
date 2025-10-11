# Installation Guide

## Basic Installation

The basic Escota installation provides the core alert system and configuration management:

```bash
pip install -e .
```

This installs only the required dependencies:
- PyYAML for configuration management

## Full Installation (with Camera Features)

To enable camera monitoring and motion detection features, you need to install OpenCV and NumPy:

```bash
pip install -e ".[full]"
```

Or manually install the optional dependencies:

```bash
pip install opencv-python numpy
```

## Development Installation

For development with testing and linting tools:

```bash
pip install -e ".[dev]"
# or
pip install -r requirements-dev.txt
```

## System Dependencies

On Linux, you may need to install system libraries for OpenCV:

```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install -y libgl1-mesa-glx libglib2.0-0

# Fedora/RHEL
sudo dnf install mesa-libGL glib2
```

## Verifying Installation

Test the basic installation:

```bash
python -c "from escota import __version__; print(__version__)"
```

Test with OpenCV features:

```bash
python -c "from escota.core.camera import CameraMonitor; print('Camera features available')"
```

## Troubleshooting

### OpenCV not available

If you see errors about OpenCV not being installed:
```
ImportError: OpenCV is required for camera monitoring. Install with: pip install opencv-python numpy
```

Solution: Install the full dependencies:
```bash
pip install opencv-python numpy
```

### Build errors during pip install

If you encounter build errors, try:
```bash
pip install --no-build-isolation -e .
```

Or use setup.py directly:
```bash
python setup.py develop
```
