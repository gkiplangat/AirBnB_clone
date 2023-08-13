#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py.
Unittest classes:
    TestFileStorageInstantiation
    TestFileStorageMethods
"""

import contextlib
import os
import unittest

import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage



class TestFileStorageInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the FileStorage class."""

    def test_file_storage_instantiation_no_args(self) -> None:
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_file_storage_instantiation_with_arg(self) -> None:
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_file_storage_file_path_private_is_str(self) -> None:
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_objects_private_is_dict(self) -> None:
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializes(self) -> None:
        self.assertEqual(type(models.storage), FileStorage)

if __name__ == "__main__":
    unittest.main()