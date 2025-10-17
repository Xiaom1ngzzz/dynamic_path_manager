API Reference
==============

This section provides detailed documentation for the Dynamic Path Manager API.

DynamicPathManager
------------------

.. autoclass:: dynamic_path_manager.DynamicPathManager
   :members:
   :undoc-members:
   :show-inheritance:

Constructor
~~~~~~~~~~~

.. automethod:: dynamic_path_manager.DynamicPathManager.__init__

Context Manager Methods
~~~~~~~~~~~~~~~~~~~~~~~

.. automethod:: dynamic_path_manager.DynamicPathManager.__enter__

.. automethod:: dynamic_path_manager.DynamicPathManager.__exit__

Utility Methods
~~~~~~~~~~~~~~~

.. automethod:: dynamic_path_manager.DynamicPathManager.get_path

.. automethod:: dynamic_path_manager.DynamicPathManager.is_path_in_sys_path

Examples
--------

Basic Usage
~~~~~~~~~~~

.. code-block:: python

   from dynamic_path_manager import DynamicPathManager

   with DynamicPathManager("./my_package") as manager:
       from my_module import some_function
       result = some_function()

Advanced Usage
~~~~~~~~~~~~~~

.. code-block:: python

   from dynamic_path_manager import DynamicPathManager

   # Custom cache clearing behavior
   with DynamicPathManager("./my_package", clear_cache=False) as manager:
       from my_module import expensive_function
       result = expensive_function()

   # Check path status
   print(f"Path: {manager.get_path()}")
   print(f"In sys.path: {manager.is_path_in_sys_path()}")

Error Handling
~~~~~~~~~~~~~~

.. code-block:: python

   from dynamic_path_manager import DynamicPathManager

   try:
       with DynamicPathManager("./nonexistent_path") as manager:
           from some_module import function
           function()
   except ImportError as e:
       print(f"Import failed: {e}")
   # Path is still cleaned up automatically
