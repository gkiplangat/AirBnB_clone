#!/usr/bin/python3
""" Defines unittests for the models/city.py."""

import unittest
import os

import re
import json
import time

from datetime import datetime
from models.city import City
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel


class TestCity(unittest.TestCase):

    """ Units to test the City Class Scenarios"""

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
        """ City class instance testing. """

        city_subclass = City()
        self.assertEqual(str(type(city_subclass)), "<class 'models.city.City'>")
        self.assertIsInstance(city_subclass, City)
        self.assertTrue(issubclass(type(city_subclass), BaseModel))

    def test_all_attributes(self):
        """ City class attributes testing. """
        attributes = storage.attributes()["City"]
        city_obj = City()
        for x, y in attributes.items():
            self.assertTrue(hasattr(city_obj, x))
            self.assertEqual(type(getattr(city_obj, x, None)), y)


if __name__ == "__main__":
    unittest.main()