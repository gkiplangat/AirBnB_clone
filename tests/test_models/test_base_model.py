#!/usr/bin/python3
"""Defines unittests for models/base_model.py.
Unittest classes:
    TestBaseModel_instantiation
    TestBaseModel_save
    TestBaseModel_to_dict
"""

import contextlib
import os
import unittest
from datetime import datetime
from time import sleep

import models
from models.base_model import BaseModel


class TestBaseModelInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class."""

    def test_no_args_instantiates(self) -> None:
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_instance_stored_in_objects(self) -> None:
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_id_is_public_str(self) -> None:
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_datetime(self) -> None:
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self) -> None:
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_models_unique_ids(self) -> None:
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_two_models_different_created_at(self) -> None:
        bm1 = BaseModel()
        sleep(0.05)
        bm2 = BaseModel()
        self.assertLess(bm1.created_at, bm2.created_at)

    def test_two_models_different_updated_at(self) -> None:
        bm1 = BaseModel()
        sleep(0.05)
        bm2 = BaseModel()
        self.assertLess(bm1.updated_at, bm2.updated_at)

    def test_str_representation(self) -> None:
        dt_obj = datetime.now()
        dt_repr = repr(dt_obj)
        base = BaseModel()
        base.id = "123456"
        base.created_at = base.updated_at = dt_obj
        bmstr = str(base)
        self.assertIn("[BaseModel] (123456)", bmstr)
        self.assertIn("'id': '123456'", bmstr)
        self.assertIn(f"'created_at': {dt_repr}", bmstr)
        self.assertIn(f"'updated_at': {dt_repr}", bmstr)

    def test_args_unused(self) -> None:
        base = BaseModel(None)
        self.assertNotIn(None, base.__dict__.values())

    def test_instantiation_with_kwargs(self) -> None:
        dt_obj = datetime.now()
        dt_iso = dt_obj.isoformat()
        base = BaseModel(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(base.id, "345")
        self.assertEqual(base.created_at, dt_obj)
        self.assertEqual(base.updated_at, dt_obj)

    def test_instantiation_with_None_kwargs(self) -> None:
        with self.assertRaises(ValueError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_args_and_kwargs(self) -> None:
        dt_obj = datetime.now()
        dt_iso = dt_obj.isoformat()
        base = BaseModel("12", id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(base.id, "345")
        self.assertEqual(base.created_at, dt_obj)
        self.assertEqual(base.updated_at, dt_obj)


class TestBaseModelSave(unittest.TestCase):
    """Unittests for testing save method of the BaseModel class."""

    def setUp(self) -> None:
        with contextlib.suppress(IOError):
            os.rename("file.json", "tmp")

    def tearDown(self) -> None:
        with contextlib.suppress(IOError):
            os.remove("file.json")
        with contextlib.suppress(IOError):
            os.rename("tmp", "file.json")

    def test_one_save(self) -> None:
        base = BaseModel()
        sleep(0.05)
        first_updated_at = base.updated_at
        base.save()
        self.assertLess(first_updated_at, base.updated_at)

    def test_two_saves(self) -> None:
        base = BaseModel()
        sleep(0.05)
        first_updated_at = base.updated_at
        base.save()
        second_updated_at = base.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        base.save()
        self.assertLess(second_updated_at, base.updated_at)

    def test_save_with_arg(self) -> None:
        base = BaseModel()
        with self.assertRaises(TypeError):
            base.save(None)

    def test_save_updates_file(self) -> None:
        base = BaseModel()
        base.save()
        bmid = f"BaseModel.{base.id}"
        with open("file.json", mode="r", encoding="utf-8") as file:
            self.assertIn(bmid, file.read())


class TestBaseModelToDict(unittest.TestCase):
    """Unittests for testing to_dict method of the BaseModel class."""

    def test_to_dict_type(self) -> None:
        base = BaseModel()
        self.assertTrue(dict, type(base.to_dict()))

    def test_to_dict_contains_correct_keys(self) -> None:
        base = BaseModel()
        self.assertIn("id", base.to_dict())
        self.assertIn("created_at", base.to_dict())
        self.assertIn("updated_at", base.to_dict())
        self.assertIn("__class__", base.to_dict())

    def test_to_dict_contains_added_attributes(self) -> None:
        base = BaseModel()
        base.name = "Holberton"
        base.my_number = 98
        self.assertIn("name", base.to_dict())
        self.assertIn("my_number", base.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self) -> None:
        base = BaseModel()
        bm_dict = base.to_dict()
        self.assertEqual(str, type(bm_dict["created_at"]))
        self.assertEqual(str, type(bm_dict["updated_at"]))

    def test_to_dict_output(self) -> None:
        dt_obj = datetime.now()
        base = BaseModel()
        base.id = "123456"
        base.created_at = base.updated_at = dt_obj
        tdict = {
            "id": "123456",
            "__class__": "BaseModel",
            "created_at": dt_obj.isoformat(),
            "updated_at": dt_obj.isoformat(),
        }
        self.assertDictEqual(base.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self) -> None:
        base = BaseModel()
        self.assertNotEqual(base.to_dict(), base.__dict__)

    def test_to_dict_with_arg(self) -> None:
        base = BaseModel()
        with self.assertRaises(TypeError):
            base.to_dict(None)


if __name__ == "__main__":
    unittest.main()
