#!/usr/bin/python3
""" Defines unittests for the models/state.py."""

import unittest
import os

import re
import json
import time

from datetime import datetime
from models.state import State
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel


class TestState(unittest.TestCase):

    """ Units to test the State Class Scenarios"""

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
        """ State class instance testing. """

        State_subclass = State()
        self.assertEqual(str(type(State_subclass)), "<class 'models.state.State'>")
        self.assertIsInstance(State_subclass, State)
        self.assertTrue(issubclass(type(State_subclass), BaseModel))

    def test_all_attributes(self):
        """ State class attributes testing. """
        attributes = storage.attributes()["State"]
        State_obj = State()
        for x, y in attributes.items():
            self.assertTrue(hasattr(State_obj, x))
            self.assertEqual(type(getattr(State_obj, x, None)), y)


if __name__ == "__main__":
    unittest.main()