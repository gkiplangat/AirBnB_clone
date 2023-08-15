#!/usr/bin/python3
""" Defines unittests for the models/review.py."""

import unittest
import os

import re
import json
import time

from datetime import datetime
from models.review import Review
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel


class TestReview(unittest.TestCase):

    """ Units to test the Review Class Scenarios"""

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
        """ Review class instance testing. """

        Review_subclass = Review()
        self.assertEqual(str(type(Review_subclass)), "<class 'models.review.Review'>")
        self.assertIsInstance(Review_subclass, Review)
        self.assertTrue(issubclass(type(Review_subclass), BaseModel))

    def test_all_attributes(self):
        """ Review class attributes testing. """
        attributes = storage.attributes()["Review"]
        Review_obj = Review()
        for x, y in attributes.items():
            self.assertTrue(hasattr(Review_obj, x))
            self.assertEqual(type(getattr(Review_obj, x, None)), y)


if __name__ == "__main__":
    unittest.main()