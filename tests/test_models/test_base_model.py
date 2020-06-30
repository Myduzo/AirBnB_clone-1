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
	

if __name__ == '__main__':
	unittest.main()
