Examples
=========

This section provides comprehensive examples of how to use Dynamic Path Manager in various scenarios.

Basic Import Example
--------------------

.. code-block:: python

   from dynamic_path_manager import DynamicPathManager

   # Simple import from a temporary path
   with DynamicPathManager("./my_package") as manager:
       from my_module import some_function
       result = some_function()
       print(f"Result: {result}")

Plugin System Example
---------------------

.. code-block:: python

   from dynamic_path_manager import DynamicPathManager
   import os

   def load_plugin(plugin_path):
       """Load a plugin from the given path."""
       with DynamicPathManager(plugin_path) as manager:
           try:
               from plugin import Plugin
               return Plugin()
           except ImportError as e:
               print(f"Failed to load plugin from {plugin_path}: {e}")
               return None

   # Load plugins from different directories
   plugins = []
   for plugin_dir in ["./plugins/plugin1", "./plugins/plugin2"]:
       if os.path.exists(plugin_dir):
           plugin = load_plugin(plugin_dir)
           if plugin:
               plugins.append(plugin)

Testing Example
---------------

.. code-block:: python

   from dynamic_path_manager import DynamicPathManager
   import unittest

   class TestWithDynamicPath(unittest.TestCase):
       def test_import_from_test_dir(self):
           with DynamicPathManager("./test_modules") as manager:
               from test_module import TestClass
               instance = TestClass()
               self.assertEqual(instance.value, "test")

   if __name__ == "__main__":
       unittest.main()

Development Workflow Example
---------------------------

.. code-block:: python

   from dynamic_path_manager import DynamicPathManager
   import os

   def switch_to_local_version(package_name, local_path):
       """Switch to a local version of a package for development."""
       if not os.path.exists(local_path):
           raise FileNotFoundError(f"Local path {local_path} does not exist")

       with DynamicPathManager(local_path) as manager:
           try:
               # Import the local version
               module = __import__(package_name)
               print(f"Using local version from {local_path}")
               return module
           except ImportError as e:
               print(f"Failed to import local version: {e}")
               return None

   # Use local version for development
   local_module = switch_to_local_version("my_package", "./local_my_package")

Microservices Example
---------------------

.. code-block:: python

   from dynamic_path_manager import DynamicPathManager
   import os

   class ServiceLoader:
       def __init__(self, services_dir):
           self.services_dir = services_dir

       def load_service(self, service_name):
           """Load a service from its directory."""
           service_path = os.path.join(self.services_dir, service_name)

           if not os.path.exists(service_path):
               raise FileNotFoundError(f"Service {service_name} not found")

           with DynamicPathManager(service_path) as manager:
               try:
                   from service import Service
                   return Service()
               except ImportError as e:
                   raise ImportError(f"Failed to load service {service_name}: {e}")

   # Load services
   loader = ServiceLoader("./services")
   user_service = loader.load_service("user_service")
   order_service = loader.load_service("order_service")

Package Management Example
--------------------------

.. code-block:: python

   from dynamic_path_manager import DynamicPathManager
   import tempfile
   import shutil

   def use_temporary_package(package_path, temp_dir=None):
       """Use a package from a temporary location."""
       if temp_dir is None:
           temp_dir = tempfile.mkdtemp()

       # Copy package to temporary location
       temp_package_path = os.path.join(temp_dir, "temp_package")
       shutil.copytree(package_path, temp_package_path)

       try:
           with DynamicPathManager(temp_package_path) as manager:
               from temp_package import main_function
               return main_function()
       finally:
           # Clean up temporary directory
           shutil.rmtree(temp_dir, ignore_errors=True)

   # Use temporary package
   result = use_temporary_package("./my_package")

Error Handling Example
----------------------

.. code-block:: python

   from dynamic_path_manager import DynamicPathManager
   import logging

   def safe_import_from_path(path, module_name, function_name):
       """Safely import a function from a module in the given path."""
       try:
           with DynamicPathManager(path) as manager:
               module = __import__(module_name)
               function = getattr(module, function_name)
               return function
       except ImportError as e:
           logging.error(f"Failed to import {function_name} from {module_name} in {path}: {e}")
           return None
       except AttributeError as e:
           logging.error(f"Function {function_name} not found in {module_name}: {e}")
           return None
       except Exception as e:
           logging.error(f"Unexpected error: {e}")
           return None

   # Safe import
   function = safe_import_from_path("./my_package", "my_module", "my_function")
   if function:
       result = function()
   else:
       print("Failed to import function")
