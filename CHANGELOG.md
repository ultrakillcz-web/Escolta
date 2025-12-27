# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2024-12-27

### Added
- **Email Notifications**: Send security alerts via email using SMTP
  - Configurable SMTP server and credentials
  - Support for multiple recipients
  - Rich email formatting with alert details
- **Database Storage**: SQLite database for persistent alert storage
  - Store and retrieve alerts from database
  - Filter alerts by type
  - Pagination support
  - Alert statistics and counts
- **Web Interface**: Browser-based dashboard for monitoring
  - Real-time alert statistics
  - Recent alerts table
  - Auto-refresh functionality
  - Clean, responsive UI
- New example scripts:
  - `database_example.py` - Database storage demonstration
  - `email_example.py` - Email notification setup
  - `webui_example.py` - Web interface demonstration
- Extended configuration options for new features

### Changed
- Updated configuration schema to include database, email, and webui settings
- Enhanced README with new feature documentation
- Updated .gitignore to exclude database files

## [0.1.0] - 2024-12-27

### Added
- Initial implementation of Escota security system
- Core modules:
  - `CameraMonitor` for video capture from cameras
  - `MotionDetector` for intelligent motion detection
  - `AlertSystem` for managing security alerts
- Configuration management with YAML support
- Command-line interface with `monitor` and `config` commands
- Comprehensive test suite with pytest
- GitHub Actions CI/CD pipeline
- Documentation:
  - README with usage examples
  - Installation guide
  - Development guide
- Code quality tools:
  - Black for code formatting
  - Flake8 for linting
  - MyPy for type checking
- Optional OpenCV dependencies for camera features
- Configuration file support (YAML format)

### Dependencies
- Core: PyYAML >= 6.0
- Optional: opencv-python >= 4.8.0, numpy >= 1.24.0
- Dev: pytest >= 7.4.0, pytest-cov >= 4.1.0, black >= 23.0.0, flake8 >= 6.0.0, mypy >= 1.5.0

[0.2.0]: https://github.com/ultrakillcz-web/Escota/releases/tag/v0.2.0
[0.1.0]: https://github.com/ultrakillcz-web/Escota/releases/tag/v0.1.0
