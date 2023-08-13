import unittest
from unittest.mock import mock_open, patch
from your_module import FileStorage


class TestFileStorage(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open, r_data='{}')
    def setUp(self, mock_file):
        self.storage = FileStorage()

    def test_all_method(self):
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict)
        self.assertEqual(all_objects, {})

    def test_new_method(self):
        class Dummy:
            def __init__(self, id):
                self.id = id
        obj = Dummy("test_id")
        self.storage.new(obj)
        all_objects = self.storage.all()
        self.assertIn("Dummy.test_id", all_objects)

    @patch('builtins.open', new_callable=mock_open)
    def test_save_method(self, mock_file):
        class Dummy:
            def __init__(self, id):
                self.id = id

                def to_dict(self):
                    return {'__class__': 'Dummy', 'id': self.id}
        obj = Dummy("test_id")
        self.storage.new(obj)
        self.storage.save()
        mock_file.assert_called_once_with(
            self.storage._FileStorage__file_path, 'w')
        handle = mock_file()
        handle.write.assert_called_once_with(
            '{"Dummy.test_id": {"__class__": "Dummy", "id": "test_id"}}')

    @patch('builtins.open', new_callable=mock_open,
           r_data='{"Dummy.test_id": {"__class__": "Dummy", "id": "test_id"}}')
    def test_reload_method(self, mock_file):
        self.storage.reload()
        all_objects = self.storage.all()
        self.assertIn("Dummy.test_id", all_objects)
        reloaded_obj = all_objects["Dummy.test_id"]
        self.assertIsInstance(reloaded_obj, Dummy)
        self.assertEqual(reloaded_obj.id, "test_id")


if __name__ == '__main__':
    unittest.main()
