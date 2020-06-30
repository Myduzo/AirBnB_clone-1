#!/usr/bin/python3
"""Module for testing the BaseModel class"""
import unittest
from models.base_model import BaseModel
import uuid
import os
import datetime

class TestBaseModel(unittest.TestCase):
	"""Tests for the BaseModel class"""

	def test_id(self):
		"""Test id"""
		test1 = BaseModel()
		test2 = BaseModel()
		self.assertNotEqual(test1.id, test2.id)

	def test_str(self):
		"""Test string"""
		test = BaseModel()
		self.assertIsInstance(test.__str__(), str)

	def test_save(self):
		"""Test save"""
		self.assertFalse(os.path.exists("file.json"))

	def test_to_dict(self):
		"""Test to dict"""
		test1 = BaseModel()
		self.assertIsInstance(test1.to_dict(), dict)
	
	def testInit(self):
		"""Test init"""
		test1 = BaseModel()
		test1.my_num = 89
		test1.my_name = "Hol"
		test2 = BaseModel(**test1.to_dict())

		self.assertEqual(test1.id, test2.id)
		self.assertEqual(test1.created_at, test2.created_at)
		self.assertEqual(test1.updated_at, test2.updated_at)
		self.assertEqual(test2.my_num, 89)
		self.assertEqual(test2.my_name, "Hol")

if __name__ == '__main__':
	unittest.main()
