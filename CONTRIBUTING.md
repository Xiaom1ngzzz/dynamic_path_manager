# Contributing to Dynamic Path Manager

Thank you for your interest in contributing to Dynamic Path Manager! This document provides guidelines and information for contributors.

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code.

## How to Contribute

### Reporting Bugs

Before creating bug reports, please check existing issues as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

- Use a clear and descriptive title
- Describe the exact steps to reproduce the problem
- Provide specific examples to demonstrate the steps
- Describe the behavior you observed after following the steps
- Explain which behavior you expected to see instead and why
- Include screenshots and animated GIFs if possible

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please include:

- Use a clear and descriptive title
- Provide a step-by-step description of the suggested enhancement
- Provide specific examples to demonstrate the steps
- Describe the current behavior and explain which behavior you expected to see instead
- Explain why this enhancement would be useful

### Pull Requests

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes
4. Add tests for your changes
5. Ensure all tests pass
6. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
7. Push to the branch (`git push origin feature/AmazingFeature`)
8. Open a Pull Request

## Development Setup

### Prerequisites

- Python 3.7 or higher
- pip
- git

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/dynamic-path-manager.git
   cd dynamic-path-manager
   ```

2. Install the package in development mode:

   ```bash
   pip install -e ".[dev]"
   ```

3. Install pre-commit hooks (optional but recommended):
   ```bash
   pre-commit install
   ```

### Running Tests

```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=dynamic_path_manager --cov-report=html

# Run specific test file
pytest tests/test_manager.py

# Run tests with verbose output
pytest -v
```

### Code Style

This project uses several tools to maintain code quality:

- **Black**: Code formatting
- **isort**: Import sorting
- **flake8**: Linting
- **mypy**: Type checking

Run all checks:

```bash
# Format code
black src/ tests/

# Sort imports
isort src/ tests/

# Lint code
flake8 src/ tests/

# Type check
mypy src/
```

### Documentation

Documentation is built using Sphinx. To build the documentation:

```bash
# Install documentation dependencies
pip install -e ".[docs]"

# Build documentation
cd docs/
make html
```

## Commit Message Guidelines

We follow conventional commit messages:

- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation only changes
- `style`: Changes that do not affect the meaning of the code
- `refactor`: A code change that neither fixes a bug nor adds a feature
- `test`: Adding missing tests or correcting existing tests
- `chore`: Changes to the build process or auxiliary tools

Examples:

- `feat: add support for Python 3.12`
- `fix: handle edge case in path resolution`
- `docs: update README with new examples`

## Release Process

1. Update version in `src/dynamic_path_manager/__init__.py`
2. Update `CHANGELOG.md`
3. Create a release tag
4. Build and upload to PyPI

## Questions?

If you have any questions about contributing, please open an issue or contact the maintainers.
