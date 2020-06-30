#!/usr/bin/python3
"""Module for testing the FileStorage class"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import uuid
import os
import datetime


class TestFileStorage(unittest.TestCase):
    """Tests for the FileStorage class"""

    def test_objects(self):
        """Test objects"""
        test = FileStorage()
        self.assertIsInstance(test._FileStorage__objects, dict)

    def test_file_path(self):
        """ Check file_path type """
        test = FileStorage()
        self.assertIsInstance(test._FileStorage__file_path, str)

    def test_file_exist(self):
        """Test exist"""
        self.assertFalse(os.path.exists("file.json"))

    def test_all(self):
        """Test all"""
        my_dict = {"Base01": {"foo1": 62, "foo2": 19, "foo3": 2},
                   "Base02": {"foo4": 30, "foo5": 89, "foo6": 56}}
        FileStorage._FileStorage__objects = my_dict
        self.assertEqual(my_dict, FileStorage().all())

    def test_new(self):
        """Test new"""
        test = BaseModel()
        my_class = FileStorage()
        my_class.new(test)

        self.assertIs(type(my_class.all()), dict)
        self.assertEqual(my_class.all()["BaseModel" + "." + test.id], test)


if __name__ == '__main__':
    unittest.main()
