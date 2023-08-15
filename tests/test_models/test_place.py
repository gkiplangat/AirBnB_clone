#!/usr/bin/python3
""" Defines unittests for the models/place.py."""

import unittest
import os

import re
import json
import time

from datetime import datetime
from models.place import Place
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):

    """ Units to test the Place Class Scenarios"""

    def setUpClass(self):
        """ Sets up set up any necessary resources."""
        pass

    def tearDownClass(self):
        """  Method to clean and reset resources used. """
        self.resetStorage()
        pass

    def resetStorage(self):
        """ Resetting changes made to FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_all_instances(self):
        """ Place class instance testing. """

        Place_subclass = Place()
        self.assertEqual(str(type(Place_subclass)), "<class 'models.place.Place'>")
        self.assertIsInstance(Place_subclass, Place)
        self.assertTrue(issubclass(type(Place_subclass), BaseModel))

    def test_all_attributes(self):
        """ Place class attributes testing. """
        attributes = storage.attributes()["Place"]
        Place_obj = Place()
        for x, y in attributes.items():
            self.assertTrue(hasattr(Place_obj, x))
            self.assertEqual(type(getattr(Place_obj, x, None)), y)


if __name__ == "__main__":
    unittest.main()