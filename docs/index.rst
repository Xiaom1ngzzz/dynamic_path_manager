Welcome to Dynamic Path Manager's documentation!
=================================================

Dynamic Path Manager is a Python context manager for temporarily adding and removing paths from ``sys.path``. This is particularly useful when you need to dynamically import modules from different directories without permanently polluting your Python path.

Features
--------

* 🚀 **Simple Context Manager**: Easy-to-use context manager interface
* 🧹 **Automatic Cleanup**: Automatically removes paths when exiting the context
* 🔄 **Module Cache Management**: Clears module cache to prevent conflicts
* 🛡️ **Safe**: Only removes paths that were added by the manager
* 📦 **Lightweight**: No external dependencies
* 🐍 **Python 3.7+**: Compatible with modern Python versions

Quick Start
-----------

.. code-block:: python

   from dynamic_path_manager import DynamicPathManager

   # Temporarily add a path to sys.path
   with DynamicPathManager("./my_package") as manager:
       from my_module import some_function
       result = some_function()
       print(f"Result: {result}")

   # Path is automatically removed from sys.path after the with block

Installation
------------

.. code-block:: bash

   pip install dynamic-path-manager

Contents
--------

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   quickstart
   api
   examples
   contributing

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
