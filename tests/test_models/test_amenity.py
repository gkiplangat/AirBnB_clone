#!/usr/bin/python3
""" Defines unittests for the models/amenity.py."""

import unittest
import os

import re
import json
import time

from datetime import datetime
from models.amenity import Amenity
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):

    """ Units to test the Amenity Class Scenarios"""

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
        """ Amenity class instance testing. """

        Amenity_subclass = Amenity()
        self.assertEqual(str(type(Amenity_subclass)), "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(Amenity_subclass, Amenity)
        self.assertTrue(issubclass(type(Amenity_subclass), BaseModel))

    def test_all_attributes(self):
        """ Amenity class attributes testing. """
        attributes = storage.attributes()["Amenity"]
        Amenity_obj = Amenity()
        for x, y in attributes.items():
            self.assertTrue(hasattr(Amenity_obj, x))
            self.assertEqual(type(getattr(Amenity_obj, x, None)), y)


if __name__ == "__main__":
    unittest.main()