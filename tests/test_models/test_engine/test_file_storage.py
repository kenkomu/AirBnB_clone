#!/usr/bin/python3
"""Unittest module for the file_storage Class."""


import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_storage = FileStorage()

    def tearDown(self):
        self.file_storage.reset()

    def test_all(self):
        all_objects = self.file_storage.all()
        self.assertIsInstance(all_objects, dict)
        self.assertEqual(all_objects, {})

    def test_new(self):
        new_obj = {'id': '123', '__class__': 'TestModel'}
        self.file_storage.new(new_obj)
        all_objects = self.file_storage.all()
        self.assertEqual(len(all_objects), 1)
        self.assertIn('TestModel.123', all_objects)
        self.assertEqual(all_objects['TestModel.123'], new_obj)

    def test_save(self):
        new_obj = {'id': '123', '__class__': 'TestModel'}
        self.file_storage.new(new_obj)
        self.file_storage.save()
        file_path = self.file_storage._FileStorage__file_path
        with open(file_path, 'r') as file:
            data = file.read()
            self.assertIn('TestModel.123', data)
            self.assertIn('"id": "123"', data)
            self.assertIn('"__class__": "TestModel"', data)

    def test_reload(self):
        new_obj = {'id': '123', '__class__': 'TestModel'}
        self.file_storage.new(new_obj)
        self.file_storage.save()
        self.file_storage.reload()
        all_objects = self.file_storage.all()
        self.assertEqual(len(all_objects), 1)
        self.assertIn('TestModel.123', all_objects)
        self.assertEqual(all_objects['TestModel.123'], new_obj)


if __name__ == '__main__':
    unittest.main()
