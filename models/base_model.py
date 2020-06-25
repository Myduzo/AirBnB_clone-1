#!/usr/bin/python3
""" Base class """
import json
import uuid
import datetime
from os import path


class BaseModel:
    """ BaseModel class"""
    def __init__(self, id=None):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def save(self):
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def to_dict(self):
        dt = dict(self.__dict__)
        dt['created_at'] = self.created_at.isoformat()
        dt['updated_at'] = self.updated_at.isoformat()
        dt["__class__"] = "BaseModel"
        return dt
