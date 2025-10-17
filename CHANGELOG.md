# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Initial project structure
- Basic DynamicPathManager implementation
- Comprehensive test suite
- Documentation and examples

## [1.0.0] - 2024-01-XX

### Added

- Initial release of DynamicPathManager
- Context manager for temporary sys.path management
- Automatic module cache cleanup
- Support for Python 3.7+
- Comprehensive documentation
- Unit tests with 100% coverage
- Example usage scripts
- MIT license

### Features

- `DynamicPathManager` class with context manager support
- Automatic path addition and removal from sys.path
- Module cache management to prevent conflicts
- Safe path management (only removes paths added by the manager)
- Support for both relative and absolute paths
- Optional cache clearing control
- Utility methods for path inspection

### Documentation

- README with quick start guide
- API reference documentation
- Usage examples
- Contributing guidelines
- Code of conduct
