Quick Start Guide
==================

This guide will help you get started with Dynamic Path Manager quickly.

Basic Usage
-----------

The most common use case is to temporarily add a directory to Python's module search path:

.. code-block:: python

   from dynamic_path_manager import DynamicPathManager

   with DynamicPathManager("./my_package") as manager:
       from my_module import some_function
       result = some_function()
       print(f"Result: {result}")

   # Path is automatically removed from sys.path after the with block

Importing from Different Directories
------------------------------------

You can use Dynamic Path Manager to import modules from different directories:

.. code-block:: python

   from dynamic_path_manager import DynamicPathManager

   # Import from directory A
   with DynamicPathManager("./examples/a") as manager:
       from utils.helper import f
       f()  # Output: a.utils.helper

   # Import from directory B
   with DynamicPathManager("./examples/b") as manager:
       from utils.helper import f
       f()  # Output: b.utils.helper

Advanced Usage
--------------

You can also control cache clearing behavior:

.. code-block:: python

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

Error Handling
--------------

Dynamic Path Manager handles errors gracefully:

.. code-block:: python

   from dynamic_path_manager import DynamicPathManager

   try:
       with DynamicPathManager("./nonexistent_path") as manager:
           from some_module import function
           function()
   except ImportError as e:
       print(f"Failed to import: {e}")
   # Path is still cleaned up even if an exception occurs

Common Use Cases
----------------

* **Plugin Systems**: Dynamically load plugins from different directories
* **Testing**: Import test modules from various locations
* **Development**: Switch between different versions of modules
* **Package Management**: Temporarily use local versions of packages
* **Microservices**: Import modules from service-specific directories
