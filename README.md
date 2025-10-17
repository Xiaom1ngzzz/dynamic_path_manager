# Dynamic Path Manager

[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](https://github.com/yourusername/dynamic-path-manager)

**Language**: [English](README.md) | [简体中文](README.zh.md)

A Python context manager for temporarily adding and removing paths from `sys.path`. This is particularly useful when you need to dynamically import modules from different directories without permanently polluting your Python path.

## Features

- 🚀 **Simple Context Manager**: Easy-to-use context manager interface
- 🧹 **Automatic Cleanup**: Automatically removes paths when exiting the context
- 🔄 **Module Cache Management**: Clears module cache to prevent conflicts
- 🛡️ **Safe**: Only removes paths that were added by the manager
- 📦 **Lightweight**: No external dependencies
- 🐍 **Python 3.7+**: Compatible with modern Python versions

## Installation

```bash
pip install dynamic-path-manager
```

Or install from source:

```bash
git clone https://github.com/yourusername/dynamic-path-manager.git
cd dynamic-path-manager
pip install -e .
```

## Quick Start

```python
from dynamic_path_manager import DynamicPathManager

# Temporarily add a path to sys.path
with DynamicPathManager("./my_package") as manager:
    from my_module import some_function
    result = some_function()
    print(f"Result: {result}")

# Path is automatically removed from sys.path after the with block
```

## Usage Examples

### Basic Usage

```python
from dynamic_path_manager import DynamicPathManager

with DynamicPathManager("./examples/a") as manager:
    from utils.helper import f
    f()  # Output: a.utils.helper

with DynamicPathManager("./examples/b") as manager:
    from utils.helper import f
    f()  # Output: b.utils.helper
```

### Advanced Usage

```python
from dynamic_path_manager import DynamicPathManager

# Disable cache clearing if you want to keep modules in memory
with DynamicPathManager("./my_package", clear_cache=False) as manager:
    from my_module import expensive_function
    result = expensive_function()

# Check if path is in sys.path
if manager.is_path_in_sys_path():
    print("Path is currently in sys.path")

# Get the managed path
print(f"Managed path: {manager.get_path()}")
```

### Error Handling

```python
from dynamic_path_manager import DynamicPathManager

try:
    with DynamicPathManager("./nonexistent_path") as manager:
        from some_module import function
        function()
except ImportError as e:
    print(f"Failed to import: {e}")
# Path is still cleaned up even if an exception occurs
```

## API Reference

### DynamicPathManager

#### `__init__(package_path: str, clear_cache: bool = True)`

Initialize the Dynamic Path Manager.

**Parameters:**

- `package_path` (str): The path to add to sys.path
- `clear_cache` (bool): Whether to clear module cache on exit (default: True)

#### `__enter__() -> DynamicPathManager`

Enter the context manager and add the path to sys.path.

**Returns:**

- `DynamicPathManager`: The instance itself

#### `__exit__(exc_type, exc_val, exc_tb) -> None`

Exit the context manager and clean up.

**Parameters:**

- `exc_type`: Exception type if an exception occurred
- `exc_val`: Exception value if an exception occurred
- `exc_tb`: Exception traceback if an exception occurred

#### `get_path() -> str`

Get the absolute path being managed.

**Returns:**

- `str`: The absolute path

#### `is_path_in_sys_path() -> bool`

Check if the managed path is currently in sys.path.

**Returns:**

- `bool`: True if the path is in sys.path, False otherwise

## Use Cases

- **Plugin Systems**: Dynamically load plugins from different directories
- **Testing**: Import test modules from various locations
- **Development**: Switch between different versions of modules
- **Package Management**: Temporarily use local versions of packages
- **Microservices**: Import modules from service-specific directories

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Development

To set up a development environment:

```bash
git clone https://github.com/yourusername/dynamic-path-manager.git
cd dynamic-path-manager
pip install -e ".[dev]"
```

Run tests:

```bash
pytest
```

Run linting:

```bash
flake8 src/
black src/
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Changelog

### 1.0.0 (2024-01-XX)

- Initial release
- Basic context manager functionality
- Module cache management
- Comprehensive documentation

## Acknowledgments

- Inspired by the need for clean dynamic imports in Python projects
- Thanks to the Python community for the excellent tooling and documentation
