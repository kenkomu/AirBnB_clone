#!/usr/bin/python3
"""Unittest module for the BaseModel Class."""

import unittest
from models.base_model import BaseModel
from models.__init__ import storage


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def tearDown(self):
        storage.reset()

    def test_save(self):
        self.base_model.save()
        objects = storage.all()
        key = self.base_model.__class__.__name__ + "." + self.base_model.id
        self.assertIn(key, objects)

    def test_to_dict(self):
        base_model_dict = self.base_model.to_dict()
        self.assertIsInstance(base_model_dict, dict)
        self.assertEqual(base_model_dict['__class__'], 'BaseModel')
        self.assertEqual(base_model_dict['id'], self.base_model.id)
        self.assertEqual(
            base_model_dict['created_at'],
            self.base_model.created_at.isoformat()
        )
        self.assertEqual(
            base_model_dict['updated_at'],
            self.base_model.updated_at.isoformat()
        )

    def test_str(self):
        base_model_str = str(self.base_model)
        self.assertIsInstance(base_model_str, str)
        self.assertIn('[BaseModel]', base_model_str)
        self.assertIn(self.base_model.id, base_model_str)
        self.assertIn(str(self.base_model.__dict__), base_model_str)


if __name__ == '__main__':
    unittest.main()