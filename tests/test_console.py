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
