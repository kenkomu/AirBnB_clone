#!/usr/bin/python3
"""Unittest module for the BaseModel Class."""

from models.base_model import BaseModel
from datetime import datetime
import json
import os
import time
import unittest
import uuid


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class"""
    def test_1_instantiation(self):
        """Tests instantiation of BaseModel class."""
        bm1 = BaseModel()
        self.assertIsInstance(bm1, BaseModel)
        self.assertTrue(hasattr(bm1, "id"))
        self.assertIsInstance(bm1.id, str)


if __name__ == '__main__':
    unittest.main()
