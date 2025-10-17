Installation
============

Installing Dynamic Path Manager is simple and straightforward.

From PyPI
---------

The recommended way to install Dynamic Path Manager is using pip:

.. code-block:: bash

   pip install dynamic-path-manager

From Source
-----------

If you want to install from source or contribute to the project:

.. code-block:: bash

   git clone https://github.com/yourusername/dynamic-path-manager.git
   cd dynamic-path-manager
   pip install -e .

Development Installation
------------------------

For development, install with development dependencies:

.. code-block:: bash

   pip install -e ".[dev]"

This will install additional tools for development including:

* pytest (testing)
* black (code formatting)
* flake8 (linting)
* mypy (type checking)
* isort (import sorting)

Requirements
------------

* Python 3.7 or higher
* No external dependencies (pure Python)

Verification
------------

To verify the installation, you can run:

.. code-block:: python

   from dynamic_path_manager import DynamicPathManager
   print("Dynamic Path Manager installed successfully!")
