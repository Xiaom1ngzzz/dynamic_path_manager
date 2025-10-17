#!/usr/bin/env python3
"""
Basic usage example of DynamicPathManager.
"""

from dynamic_path_manager import DynamicPathManager


def main():
    """Demonstrate basic usage of DynamicPathManager."""
    print("=== Basic Usage Example ===")

    # Example 1: Import from different directories
    print("\n1. Importing from different directories:")

    with DynamicPathManager("./examples/a") as manager:
        from utils.helper import f
        print("Successfully imported module from examples/a")
        f()  # Output: a.utils.helper

    with DynamicPathManager("./examples/b") as manager:
        from utils.helper import f
        print("Successfully imported module from examples/b")
        f()  # Output: b.utils.helper

    print("\n2. Path management:")

    # Example 2: Check path management
    with DynamicPathManager("./examples/a") as manager:
        print(f"Managed path: {manager.get_path()}")
        print(f"Is path in sys.path: {manager.is_path_in_sys_path()}")

    print("\n3. Error handling:")

    # Example 3: Error handling
    try:
        with DynamicPathManager("./nonexistent_path") as manager:
            from some_module import function
            function()
    except ImportError as e:
        print(f"Import failed as expected: {e}")

    print("\n=== Example completed ===")


if __name__ == "__main__":
    main()
