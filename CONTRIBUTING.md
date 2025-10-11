# Contributing to Escota

Thank you for your interest in contributing to Escota! This document provides guidelines for contributing to the project.

## Code of Conduct

Please be respectful and constructive in all interactions.

## How to Contribute

### Reporting Bugs

1. Check if the bug has already been reported in [Issues](https://github.com/ultrakillcz-web/Escota/issues)
2. If not, create a new issue with:
   - Clear title and description
   - Steps to reproduce
   - Expected vs actual behavior
   - Environment details (OS, Python version, etc.)

### Suggesting Features

1. Check existing issues and pull requests
2. Create an issue describing:
   - The problem your feature would solve
   - How it should work
   - Any alternatives you've considered

### Pull Requests

1. **Fork** the repository
2. **Create a branch** for your feature:
   ```bash
   git checkout -b feature/my-new-feature
   ```

3. **Make your changes**:
   - Write clear, documented code
   - Follow the existing code style
   - Add tests for new functionality
   - Update documentation as needed

4. **Test your changes**:
   ```bash
   # Run tests
   pytest
   
   # Check formatting
   black --check src tests
   
   # Run linter
   flake8 src tests
   ```

5. **Commit your changes**:
   ```bash
   git commit -m "Add feature: description of your feature"
   ```

6. **Push to your fork**:
   ```bash
   git push origin feature/my-new-feature
   ```

7. **Create a Pull Request** on GitHub

### Code Style

- Follow PEP 8 style guide
- Use `black` for code formatting (100 char line length)
- Use type hints where appropriate
- Write docstrings for all public functions and classes
- Keep functions focused and modular

### Testing

- Write tests for all new functionality
- Aim for >80% code coverage
- Tests should be clear and maintainable
- Use pytest fixtures where appropriate

### Documentation

- Update README.md for user-facing changes
- Update docstrings for API changes
- Add entries to CHANGELOG.md
- Update relevant guides in docs/

## Development Setup

See [DEVELOPMENT.md](docs/DEVELOPMENT.md) for detailed setup instructions.

## Questions?

Feel free to open an issue for any questions about contributing.

Thank you for helping make Escota better!
