# Development Guide

## Setting Up Development Environment

1. Clone the repository:
```bash
git clone https://github.com/ultrakillcz-web/Escota.git
cd Escota
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install in development mode:
```bash
pip install -e ".[dev,full]"
```

## Code Quality

### Formatting

We use `black` for code formatting:

```bash
# Check formatting
black --check src tests

# Apply formatting
black src tests
```

### Linting

We use `flake8` for linting:

```bash
# Check for errors
flake8 src --count --select=E9,F63,F7,F82 --show-source --statistics

# Full lint check
flake8 src --count --max-complexity=10 --max-line-length=100 --statistics
```

### Type Checking

We use `mypy` for static type checking:

```bash
mypy src --ignore-missing-imports
```

## Running Tests

### Run all tests:
```bash
pytest
```

### Run with coverage:
```bash
pytest --cov=escota --cov-report=term-missing
```

### Run specific test file:
```bash
pytest tests/test_alert.py -v
```

### Run specific test:
```bash
pytest tests/test_alert.py::TestAlertSystem::test_create_alert -v
```

## Project Structure

```
Escota/
├── src/escota/          # Main package
│   ├── __init__.py      # Package initialization
│   ├── cli.py           # Command-line interface
│   ├── core/            # Core modules
│   │   ├── __init__.py
│   │   ├── camera.py    # Camera monitoring (requires OpenCV)
│   │   ├── detector.py  # Motion detection (requires OpenCV)
│   │   └── alert.py     # Alert system
│   └── utils/           # Utilities
│       ├── __init__.py
│       └── config.py    # Configuration management
├── tests/               # Test suite
│   ├── __init__.py
│   ├── test_camera.py
│   ├── test_detector.py
│   ├── test_alert.py
│   └── test_config.py
├── config/              # Configuration files
│   └── escota.yaml      # Default configuration
├── docs/                # Documentation
├── .github/workflows/   # CI/CD pipelines
│   └── ci.yml           # GitHub Actions CI
├── pyproject.toml       # Project metadata and build config
├── setup.py             # Setup script
├── requirements.txt     # Core dependencies
└── requirements-dev.txt # Development dependencies
```

## Adding New Features

1. **Create a new module** in `src/escota/core/` or `src/escota/utils/`
2. **Write tests** in `tests/` (aim for >80% coverage)
3. **Update documentation** in the README or docs/
4. **Format and lint** your code
5. **Run tests** to ensure nothing breaks
6. **Submit a pull request**

## Testing Camera Features

Since camera and motion detection features require OpenCV, tests for these modules are skipped when OpenCV is not installed. To test these features:

1. Install OpenCV:
```bash
pip install opencv-python numpy
```

2. Run camera-specific tests:
```bash
pytest tests/test_camera.py tests/test_detector.py -v
```

Note: These tests may fail if no camera device is available. Consider mocking `cv2.VideoCapture` for unit tests.

## Continuous Integration

The project uses GitHub Actions for CI. The workflow:

1. Runs on Python 3.8, 3.9, 3.10, and 3.11
2. Installs system dependencies for OpenCV
3. Runs linters (flake8, black, mypy)
4. Runs tests with coverage
5. Uploads coverage to Codecov
6. Builds distribution packages

See `.github/workflows/ci.yml` for details.

## Release Process

1. Update version in `src/escota/__init__.py` and `pyproject.toml`
2. Update CHANGELOG.md
3. Create a git tag:
```bash
git tag -a v0.2.0 -m "Release v0.2.0"
git push origin v0.2.0
```
4. Build and publish to PyPI:
```bash
python -m build
twine upload dist/*
```
