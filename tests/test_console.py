#!/usr/bin/python3

import unittest
from unittest.mock import patch
import io
import sys
import console  # Import the console module


class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.console = console.HBNBCommand()
        self.patcher = patch('builtins.input')
        self.mock_input = self.patcher.start()

    def tearDown(self):
        self.patcher.stop()

    def test_quit_command(self):
        self.assertTrue(self.console.onecmd("quit"))

    def test_EOF_command(self):
        self.assertTrue(self.console.onecmd("EOF"))

    def test_empty_line(self):
        self.assertIsNone(self.console.onecmd(""))

    def test_help_command(self):
        expected_output = (
            "Documented commands (type help <topic>):\n"
            "========================================\n"
            "EOF  help  quit"
            )

        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("help"))
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, expected_output)

    def test_help_quit_command(self):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("help quit"))
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "Quit command to exit the program")


if __name__ == '__main__':
    unittest.main()
