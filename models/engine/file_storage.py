#!/usr/bin/python3
""" Base class """
import json
from os import path
import datetime

class FileStorage:
    """ FileStorage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        x = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[x] = obj.__dict__

    def save(self):
        if self.__file_path:
            cp_dict = dict(FileStorage.__objects)
            for key, value in cp_dict.items():
                if type(value["created_at"]) is not str:
                    value["created_at"] = value["created_at"].isoformat()
                    value["updated_at"] = value["updated_at"].isoformat()
            j_str = json.dumps(cp_dict)
            with open(self.__file_path, mode='w', encoding='utf-8') as f:
                f.write(j_str)

    def reload(self):
        if self.__file_path and path.exists(self.__file_path):
            with open(self.__file_path, encoding='utf-8') as f:
                FileStorage.__objects = json.loads(f.read())
