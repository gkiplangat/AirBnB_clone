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


class TestFileStorageMethods(unittest.TestCase):
    """Unittests for testing methods of the FileStorage class."""

    def setUp(self) -> None:
        self.base = BaseModel()
        self.user = User()
        self.state = State()
        self.place = Place()
        self.city = City()
        self.amenity = Amenity()
        self.review = Review()
        models.storage.new(self.base)
        models.storage.new(self.user)
        models.storage.new(self.state)
        models.storage.new(self.place)
        models.storage.new(self.city)
        models.storage.new(self.amenity)
        models.storage.new(self.review)
        # return super().setUp()

    @classmethod
    def setUpClass(cls) -> None:
        with contextlib.suppress(IOError):
            os.rename("file.json", "tmp")

    @classmethod
    def tearDownClass(cls) -> None:
        with contextlib.suppress(IOError):
            os.remove("file.json")
        with contextlib.suppress(IOError):
            os.rename("tmp", "file.json")
        FileStorage._FileStorage__objects = {}

    def test_all(self) -> None:
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_with_arg(self) -> None:
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self) -> None:
        self.assertIn(f"BaseModel.{self.base.id}", models.storage.all().keys())
        self.assertIn(self.base, models.storage.all().values())
        self.assertIn(f"User.{self.user.id}", models.storage.all().keys())
        self.assertIn(self.user, models.storage.all().values())
        self.assertIn(f"State.{self.state.id}", models.storage.all().keys())
        self.assertIn(self.state, models.storage.all().values())
        self.assertIn(f"Place.{self.place.id}", models.storage.all().keys())
        self.assertIn(self.place, models.storage.all().values())
        self.assertIn(f"City.{self.city.id}", models.storage.all().keys())
        self.assertIn(self.city, models.storage.all().values())
        self.assertIn(
            f"Amenity.{self.amenity.id}", models.storage.all().keys()
        )
        self.assertIn(self.amenity, models.storage.all().values())
        self.assertIn(f"Review.{self.review.id}", models.storage.all().keys())
        self.assertIn(self.review, models.storage.all().values())

    def test_new_with_args(self) -> None:
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_new_with_none(self) -> None:
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save(self) -> None:
        models.storage.save()
        save_text = ""
        with open("file.json", mode="r", encoding="utf-8") as file:
            save_text = file.read()
            self.assertIn(f"BaseModel.{self.base.id}", save_text)
            self.assertIn(f"User.{self.user.id}", save_text)
            self.assertIn(f"State.{self.state.id}", save_text)
            self.assertIn(f"Place.{self.place.id}", save_text)
            self.assertIn(f"City.{self.city.id}", save_text)
            self.assertIn(f"Amenity.{self.amenity.id}", save_text)
            self.assertIn(f"Review.{self.review.id}", save_text)

    def test_save_with_arg(self) -> None:
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self) -> None:
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn(f"BaseModel.{self.base.id}", objs)
        self.assertIn(f"User.{self.user.id}", objs)
        self.assertIn(f"State.{self.state.id}", objs)
        self.assertIn(f"Place.{self.place.id}", objs)
        self.assertIn(f"City.{self.city.id}", objs)
        self.assertIn(f"Amenity.{self.amenity.id}", objs)
        self.assertIn(f"Review.{self.review.id}", objs)

    def test_reload_no_file(self) -> None:
        self.assertIsNone(models.storage.reload())

    def test_reload_with_arg(self) -> None:
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()