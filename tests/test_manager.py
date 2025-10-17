"""
Tests for DynamicPathManager.
"""

import os
import sys
import tempfile
import pytest
from pathlib import Path

from dynamic_path_manager import DynamicPathManager


class TestDynamicPathManager:
    """Test cases for DynamicPathManager."""

    def setup_method(self):
        """Set up test fixtures."""
        self.original_sys_path = sys.path.copy()
        self.original_modules = sys.modules.copy()

    def teardown_method(self):
        """Clean up after tests."""
        sys.path.clear()
        sys.path.extend(self.original_sys_path)
        sys.modules.clear()
        sys.modules.update(self.original_modules)

    def test_init_with_relative_path(self):
        """Test initialization with relative path."""
        manager = DynamicPathManager("./test_path")
        assert os.path.isabs(manager.package_path)
        assert manager.package_path.endswith("test_path")
        assert not manager._was_in_path

    def test_init_with_absolute_path(self):
        """Test initialization with absolute path."""
        abs_path = "/tmp/test_path"
        manager = DynamicPathManager(abs_path)
        assert manager.package_path == abs_path

    def test_context_manager_adds_path(self):
        """Test that context manager adds path to sys.path."""
        with tempfile.TemporaryDirectory() as temp_dir:
            manager = DynamicPathManager(temp_dir)

            assert temp_dir not in sys.path

            with manager:
                assert temp_dir in sys.path
                assert sys.path[0] == temp_dir  # Should be at the beginning

            assert temp_dir not in sys.path

    def test_context_manager_removes_path_on_exit(self):
        """Test that path is removed on exit."""
        with tempfile.TemporaryDirectory() as temp_dir:
            with DynamicPathManager(temp_dir):
                pass

            assert temp_dir not in sys.path

    def test_path_already_in_sys_path(self):
        """Test behavior when path is already in sys.path."""
        with tempfile.TemporaryDirectory() as temp_dir:
            sys.path.insert(0, temp_dir)

            with DynamicPathManager(temp_dir) as manager:
                assert manager._was_in_path
                # Path should still be in sys.path
                assert temp_dir in sys.path

            # Path should still be in sys.path since it was there originally
            assert temp_dir in sys.path

    def test_exception_handling(self):
        """Test that path is removed even when exception occurs."""
        with tempfile.TemporaryDirectory() as temp_dir:
            try:
                with DynamicPathManager(temp_dir):
                    assert temp_dir in sys.path
                    raise ValueError("Test exception")
            except ValueError:
                pass

            assert temp_dir not in sys.path

    def test_get_path(self):
        """Test get_path method."""
        with tempfile.TemporaryDirectory() as temp_dir:
            manager = DynamicPathManager(temp_dir)
            assert manager.get_path() == temp_dir

    def test_is_path_in_sys_path(self):
        """Test is_path_in_sys_path method."""
        with tempfile.TemporaryDirectory() as temp_dir:
            manager = DynamicPathManager(temp_dir)

            assert not manager.is_path_in_sys_path()

            with manager:
                assert manager.is_path_in_sys_path()

            assert not manager.is_path_in_sys_path()

    def test_clear_cache_disabled(self):
        """Test behavior when cache clearing is disabled."""
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create a test module
            test_module_path = Path(temp_dir) / "test_module.py"
            test_module_path.write_text("def test_function(): return 'test'")

            with DynamicPathManager(temp_dir, clear_cache=False):
                import test_module
                assert test_module.test_function() == 'test'

            # Module should still be in cache
            assert 'test_module' in sys.modules

    def test_clear_cache_enabled(self):
        """Test behavior when cache clearing is enabled."""
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create a test module
            test_module_path = Path(temp_dir) / "test_module.py"
            test_module_path.write_text("def test_function(): return 'test'")

            with DynamicPathManager(temp_dir, clear_cache=True):
                import test_module
                assert test_module.test_function() == 'test'

            # Module should be removed from cache
            assert 'test_module' not in sys.modules

    def test_multiple_contexts(self):
        """Test multiple nested contexts."""
        with tempfile.TemporaryDirectory() as temp_dir1, \
             tempfile.TemporaryDirectory() as temp_dir2:

            with DynamicPathManager(temp_dir1):
                assert temp_dir1 in sys.path
                assert sys.path[0] == temp_dir1

                with DynamicPathManager(temp_dir2):
                    assert temp_dir2 in sys.path
                    assert sys.path[0] == temp_dir2
                    assert temp_dir1 in sys.path

                assert temp_dir1 in sys.path
                assert temp_dir2 not in sys.path

            assert temp_dir1 not in sys.path
            assert temp_dir2 not in sys.path

    def test_return_self(self):
        """Test that __enter__ returns self."""
        with tempfile.TemporaryDirectory() as temp_dir:
            manager = DynamicPathManager(temp_dir)

            with manager as entered_manager:
                assert entered_manager is manager
