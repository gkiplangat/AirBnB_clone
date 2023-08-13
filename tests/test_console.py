#!/usr/bin/python3
"""Defines unittests for console.py.
Unittest classes:
    TestHBNBCommand_prompting
    TestHBNBCommand_help
    TestHBNBCommand_exit
    TestHBNBCommand_create
    TestHBNBCommand_show
    TestHBNBCommand_all
    TestHBNBCommand_destroy
    TestHBNBCommand_update
"""
import os
import unittest
from io import StringIO
from unittest.mock import patch

from console import HBNBCommand
from models import storage
from models.engine.file_storage import FileStorage


class TestHBNBCommandPrompt(unittest.TestCase):
    """
    Unittests for testing prompting of the HBNB command interpreter.
    """

    def test_prompt_string(self) -> None:
        """..."""
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_empty_line(self) -> None:
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())


class TestHBNBCommandHelp(unittest.TestCase):
    """Unittests for testing help messages of the HBNB command interpreter."""

    def test_help_quit(self) -> None:
        """..."""
        hhbelp = "Quit command to exit the program"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(hhbelp, output.getvalue().strip())

    def test_help_create(self) -> None:
        """..."""
        hhbelp = "Usage: create <class_name>"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertEqual(hhbelp, output.getvalue().strip())

    def test_help_EOF(self) -> None:
        """..."""
        hhbelp = "Cleanly exits from the interpreter"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(hhbelp, output.getvalue().strip())

    def test_help_show(self) -> None:
        hhbelp = "Usage: show <class_name> <id> or <class>.show(<id>)"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help show"))
            self.assertEqual(hhbelp, output.getvalue().strip())

    def test_help_destroy(self) -> None:
        hhbelp = (
            "Usage: destroy <class_name> <id> or <class>.destroy(<id>)\n"
            "Removes the specified class"
        )
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help destroy"))
            self.assertEqual(hhbelp, output.getvalue().strip())

    def test_help_all(self) -> None:
        hhbelp = "Usage: all or all <class> or <class>.all()"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertEqual(hhbelp, output.getvalue().strip())


class TestHBNBCommandExit(unittest.TestCase):
    """Unittests for testing exiting from the HBNB command interpreter."""

    def test_quit_exits(self) -> None:
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF_exits(self) -> None:
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("EOF"))


class TestHBNBCommandCreate(unittest.TestCase):
    """Unittests for testing create from the HBNB command interpreter."""

    @classmethod
    def setUp(self) -> None:
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self) -> None:
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_create_missing_class(self) -> None:
        correct = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_create_invalid_class(self) -> None:
        correct = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create MyModel"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_create_object(self) -> None:
        """..."""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertLess(0, len(output.getvalue().strip()))
            test_key = "BaseModel.{}".format(output.getvalue().strip())
            self.assertIn(test_key, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertLess(0, len(output.getvalue().strip()))
            test_key = "User.{}".format(output.getvalue().strip())
            self.assertIn(test_key, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertLess(0, len(output.getvalue().strip()))
            test_key = "State.{}".format(output.getvalue().strip())
            self.assertIn(test_key, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertLess(0, len(output.getvalue().strip()))
            test_key = "City.{}".format(output.getvalue().strip())
            self.assertIn(test_key, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertLess(0, len(output.getvalue().strip()))
            test_key = "Amenity.{}".format(output.getvalue().strip())
            self.assertIn(test_key, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertLess(0, len(output.getvalue().strip()))
            test_key = "Place.{}".format(output.getvalue().strip())
            self.assertIn(test_key, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            self.assertLess(0, len(output.getvalue().strip()))
            test_key = "Review.{}".format(output.getvalue().strip())
            self.assertIn(test_key, storage.all().keys())


class TestHBNBCommandShow(unittest.TestCase):
    """Unittests for testing show from the HBNB command interpreter"""

    @classmethod
    def setUp(self) -> None:
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self) -> None:
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_show_missing_class(self) -> None:
        correct = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(".show()"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_show_invalid_class(self) -> None:
        correct = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show MyModel"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("MyModel.show()"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_show_missing_id_space_notation(self) -> None:
        correct = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show User"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show State"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show City"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show Amenity"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show Place"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show Review"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_show_missing_id_dot_notation(self) -> None:
        correct = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.show()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.show()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.show()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.show()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.show()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.show()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.show()"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_show_no_instance_found_space_notation(self) -> None:
        correct = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show User 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show State 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show City 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show Amenity 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show Place 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show Review 1"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_show_no_instance_found_dot_notation(self) -> None:
        correct = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.show(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.show(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.show(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.show(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.show(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.show(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.show(1)"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_show_objects_space_notation(self) -> None:
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            test_id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["BaseModel.{}".format(test_id)]
            command = "show BaseModel {}".format(test_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            test_id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["User.{}".format(test_id)]
            command = "show User {}".format(test_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            test_id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["State.{}".format(test_id)]
            command = "show State {}".format(test_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            test_id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["Place.{}".format(test_id)]
            command = "show Place {}".format(test_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            test_id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["City.{}".format(test_id)]
            command = "show City {}".format(test_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            test_id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["Amenity.{}".format(test_id)]
            command = "show Amenity {}".format(test_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            test_id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["Review.{}".format(test_id)]
            command = "show Review {}".format(test_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())


class TestHBNBCommandDestroy(unittest.TestCase):
    """Unittests for testing destroy from the HBNB command interpreter."""

    @classmethod
    def setUp(self) -> None:
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self) -> None:
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        storage.reload()

    def test_destroy_missing_class(self) -> None:
        correct = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_destroy_invalid_class(self) -> None:
        correct = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy MyModel"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("MyModel.destroy()"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_destroy_id_missing_space_notation(self) -> None:
        correct = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy User"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy State"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy City"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy Amenity"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy Place"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy Review"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_destroy_id_missing_dot_notation(self) -> None:
        correct = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.destroy()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.destroy()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.destroy()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.destroy()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.destroy()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.destroy()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.destroy()"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_destroy_invalid_id_space_notation(self) -> None:
        correct = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy User 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy State 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy City 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy Amenity 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy Place 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy Review 1"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_destroy_invalid_id_dot_notation(self) -> None:
        correct = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.destroy(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.destroy(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.destroy(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.destroy(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.destroy(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.destroy(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.destroy(1)"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_destroy_objects_space_notation(self) -> None:
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            test_id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["BaseModel.{}".format(test_id)]
            command = "destroy BaseModel {}".format(test_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            test_id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["User.{}".format(test_id)]
            command = "show User {}".format(test_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            test_id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["State.{}".format(test_id)]
            command = "show State {}".format(test_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            test_id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["Place.{}".format(test_id)]
            command = "show Place {}".format(test_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            test_id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["City.{}".format(test_id)]
            command = "show City {}".format(test_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            test_id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["Amenity.{}".format(test_id)]
            command = "show Amenity {}".format(test_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            test_id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["Review.{}".format(test_id)]
            command = "show Review {}".format(test_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())

    def test_destroy_objects_dot_notation(self) -> None:
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            test_id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["BaseModel.{}".format(test_id)]
            command = "BaseModel.destroy({})".format(test_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            test_id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["User.{}".format(test_id)]
            command = "User.destroy({})".format(test_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            test_id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["State.{}".format(test_id)]
            command = "State.destroy({})".format(test_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            test_id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["Place.{}".format(test_id)]
            command = "Place.destroy({})".format(test_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            test_id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["City.{}".format(test_id)]
            command = "City.destroy({})".format(test_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            test_id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["Amenity.{}".format(test_id)]
            command = "Amenity.destroy({})".format(test_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            test_id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["Review.{}".format(test_id)]
            command = "Review.destory({})".format(test_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())


class TestHBNBCommandAll(unittest.TestCase):
    """Unittests for testing all of the HBNB command interpreter."""

    @classmethod
    def setUp(self) -> None:
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self) -> None:
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_all_invalid_class(self) -> None:
        correct = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all MyModel"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all ALX"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_all_objects_space_notation(self) -> None:
        with patch("sys.stdout", new=StringIO()) as output:
            self.create_all_objects()
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all"))
            self.assertIn("BaseModel", output.getvalue().strip())
            self.assertIn("User", output.getvalue().strip())
            self.assertIn("State", output.getvalue().strip())
            self.assertIn("Place", output.getvalue().strip())
            self.assertIn("City", output.getvalue().strip())
            self.assertIn("Amenity", output.getvalue().strip())
            self.assertIn("Review", output.getvalue().strip())

    # TODO Rename this here and in `test_all_objects_space_notation`
    def create_all_objects(self) -> None:
        self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
        self.assertFalse(HBNBCommand().onecmd("create User"))
        self.assertFalse(HBNBCommand().onecmd("create State"))
        self.assertFalse(HBNBCommand().onecmd("create Place"))
        self.assertFalse(HBNBCommand().onecmd("create City"))
        self.assertFalse(HBNBCommand().onecmd("create Amenity"))
        self.assertFalse(HBNBCommand().onecmd("create Review"))

    def test_all_single_object_space_notation(self) -> None:
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all BaseModel"))
            self.assertIn("BaseModel", output.getvalue().strip())
            self.assertNotIn("User", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all User"))
            self.assertIn("User", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all State"))
            self.assertIn("State", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all City"))
            self.assertIn("City", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all Amenity"))
            self.assertIn("Amenity", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all Place"))
            self.assertIn("Place", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all Review"))
            self.assertIn("Review", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())

    def test_all_single_object_dot_notation(self) -> None:
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.all()"))
            self.assertIn("BaseModel", output.getvalue().strip())
            self.assertNotIn("User", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.all()"))
            self.assertIn("User", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.all()"))
            self.assertIn("State", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.all()"))
            self.assertIn("City", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.all()"))
            self.assertIn("Amenity", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.all()"))
            self.assertIn("Place", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.all()"))
            self.assertIn("Review", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())


class TestHBNBCommandUpdate(unittest.TestCase):
    """Unittests for testing update from the HBNB command interpreter."""

    @classmethod
    def setUp(self) -> None:
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self) -> None:
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_update_missing_class(self) -> None:
        correct = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(".update()"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_update_invalid_class(self) -> None:
        correct = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update MyModel"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("MyModel.update()"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_update_missing_id_space_notation(self) -> None:
        correct = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update BaseModel"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update User"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update State"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update City"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update Amenity"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update Place"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update Review"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_update_missing_id_dot_notation(self) -> None:
        correct = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.update()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.update()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.update()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.update()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.update()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.update()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.update()"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_update_invalid_id_space_notation(self) -> None:
        correct = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update BaseModel 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update User 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update State 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update City 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update Amenity 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update Place 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update Review 1"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_update_invalid_id_dot_notation(self) -> None:
        correct = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.update(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.update(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.update(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.update(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.update(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.update(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.update(1)"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_update_missing_attr_name_space_notation(self) -> None:
        correct = "** attribute name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            test_id = output.getvalue().strip()
            test_cmd = "update BaseModel {}".format(test_id)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(test_cmd))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            test_id = output.getvalue().strip()
            test_cmd = "update User {}".format(test_id)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(test_cmd))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            test_id = output.getvalue().strip()
            test_cmd = "update State {}".format(test_id)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(test_cmd))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            test_id = output.getvalue().strip()
            test_cmd = "update City {}".format(test_id)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(test_cmd))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            test_id = output.getvalue().strip()
            test_cmd = "update Amenity {}".format(test_id)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(test_cmd))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            test_id = output.getvalue().strip()
            test_cmd = "update Place {}".format(test_id)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(test_cmd))
            self.assertEqual(correct, output.getvalue().strip())

    def test_update_missing_attr_name_dot_notation(self) -> None:
        correct = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            test_id = output.getvalue().strip()
            test_cmd = "BaseModel.update({})".format(test_id)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(test_cmd))
            # print(f">>>>>>>>>>>>>>>>>>{test_id}")
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            test_id = output.getvalue().strip()
            test_cmd = "User.update({})".format(test_id)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(test_cmd))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            test_id = output.getvalue().strip()
            test_cmd = "State.update({})".format(test_id)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(test_cmd))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            test_id = output.getvalue().strip()
            test_cmd = "City.update({})".format(test_id)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(test_cmd))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            test_id = output.getvalue().strip()
            test_cmd = "Amenity.update({})".format(test_id)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(test_cmd))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            test_id = output.getvalue().strip()
            test_cmd = "Place.update({})".format(test_id)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(test_cmd))
            self.assertEqual(correct, output.getvalue().strip())

    def test_update_missing_attr_value_space_notation(self) -> None:
        correct = "** value missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            test_id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            test_cmd = "update BaseModel {} attr_name".format(test_id)
            self.assertFalse(HBNBCommand().onecmd(test_cmd))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            test_id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            test_cmd = "update User {} attr_name".format(test_id)
            self.assertFalse(HBNBCommand().onecmd(test_cmd))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create State")
            test_id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            test_cmd = "update State {} attr_name".format(test_id)
            self.assertFalse(HBNBCommand().onecmd(test_cmd))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create City")
            test_id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            test_cmd = "update City {} attr_name".format(test_id)
            self.assertFalse(HBNBCommand().onecmd(test_cmd))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Amenity")
            test_id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            test_cmd = "update Amenity {} attr_name".format(test_id)
            self.assertFalse(HBNBCommand().onecmd(test_cmd))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            test_id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            test_cmd = "update Place {} attr_name".format(test_id)
            self.assertFalse(HBNBCommand().onecmd(test_cmd))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Review")
            test_id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            test_cmd = "update Review {} attr_name".format(test_id)
            self.assertFalse(HBNBCommand().onecmd(test_cmd))
            self.assertEqual(correct, output.getvalue().strip())


class TestHBNBCommandCount(unittest.TestCase):
    """Unittests for testing count method of HBNB comand interpreter."""

    @classmethod
    def setUp(self) -> None:
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    @classmethod
    def tearDown(self) -> None:
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_count_object(self) -> None:
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.count()"))
            self.assertEqual("1", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.count()"))
            self.assertEqual("1", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.count()"))
            self.assertEqual("1", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.count()"))
            self.assertEqual("1", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.count()"))
            self.assertEqual("1", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.count()"))
            self.assertEqual("1", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.count()"))
            self.assertEqual("1", output.getvalue().strip())


if __name__ == "__main__":
    unittest.main()