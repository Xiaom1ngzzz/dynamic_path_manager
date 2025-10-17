"""
Dynamic Path Manager implementation.
"""

import sys
import os
from typing import Optional, Any


class DynamicPathManager:
    """
    A context manager for temporarily adding and removing paths from sys.path.

    This class allows you to temporarily add a directory to Python's module search path,
    import modules from that directory, and then cleanly remove the path when done.
    It also handles module cache cleanup to prevent conflicts when switching between
    different directories with similar module names.

    Example:
        >>> with DynamicPathManager("./my_package") as manager:
        ...     from my_module import some_function
        ...     some_function()
        # Path is automatically removed from sys.path after the with block
    """

    def __init__(self, package_path: str, clear_cache: bool = True):
        """
        Initialize the Dynamic Path Manager.

        Args:
            package_path (str): The path to add to sys.path
            clear_cache (bool): Whether to clear module cache on exit (default: True)
        """
        self.package_path = os.path.abspath(package_path)
        self.clear_cache = clear_cache
        self._was_in_path = False
        self._added_modules = set()

    def __enter__(self) -> 'DynamicPathManager':
        """
        Enter the context manager and add the path to sys.path.

        Returns:
            DynamicPathManager: The instance itself
        """
        if self.package_path not in sys.path:
            sys.path.insert(0, self.package_path)
            self._was_in_path = False
        else:
            self._was_in_path = True
        return self

    def __exit__(self, exc_type: Optional[type], exc_val: Optional[Exception],
                 exc_tb: Optional[Any]) -> None:
        """
        Exit the context manager and clean up.

        Args:
            exc_type: Exception type if an exception occurred
            exc_val: Exception value if an exception occurred
            exc_tb: Exception traceback if an exception occurred
        """
        # Remove path from sys.path if we added it
        if not self._was_in_path and self.package_path in sys.path:
            sys.path.remove(self.package_path)

        # Clear module cache if requested
        if self.clear_cache:
            self._clear_module_cache()

    def _clear_module_cache(self) -> None:
        """
        Clear modules from sys.modules that might conflict with future imports.
        This is a conservative approach that only removes modules that were likely
        imported from the temporary path.
        """
        # Get the package name from the path
        package_name = os.path.basename(self.package_path)

        # Find modules to remove
        modules_to_remove = []
        for module_name in list(sys.modules.keys()):
            # Remove modules that start with the package name
            if module_name.startswith(package_name):
                modules_to_remove.append(module_name)
            # Also remove common module names that might conflict
            elif module_name in ['utils', 'helpers', 'common']:
                modules_to_remove.append(module_name)

        # Remove the modules
        for module_name in modules_to_remove:
            if module_name in sys.modules:
                del sys.modules[module_name]

    def get_path(self) -> str:
        """
        Get the absolute path being managed.

        Returns:
            str: The absolute path
        """
        return self.package_path

    def is_path_in_sys_path(self) -> bool:
        """
        Check if the managed path is currently in sys.path.

        Returns:
            bool: True if the path is in sys.path, False otherwise
        """
        return self.package_path in sys.path
