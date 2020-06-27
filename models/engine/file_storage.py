#!/usr/bin/python3
""" Base class """
import json
from os import path
import datetime
import copy


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
            cp_dict = copy.deepcopy(FileStorage.__objects)
            for key, value in cp_dict.items():
                if type(value["created_at"]) is not str:
                    value["created_at"] = value["created_at"].isoformat()
                    value["updated_at"] = value["updated_at"].isoformat()
            j_str = json.dumps(cp_dict)
            with open(self.__file_path, mode='w', encoding='utf-8') as f:
                f.write(j_str)

    def reload(self):
        if FileStorage.__file_path and path.exists(
                FileStorage.__file_path
        ) and path.getsize(FileStorage.__file_path):
            with open(self.__file_path, encoding='utf-8') as f:
                tmp = json.loads(f.read())
                for key, value in tmp.items():
                    i = 0
                    conver_value = value["created_at"]
                    while (i < 2):
                        conver_value, _, us = conver_value.partition(".")
                        conver_value = datetime.datetime.strptime(
                            conver_value,
                            '%Y-%m-%dT%H:%M:%S'
                        )
                        us = int(us.rstrip("Z"), 10)
                        conver_value = conver_value + datetime.timedelta(
                            microseconds=us
                        )
                        if i == 0:
                            value["created_at"] = conver_value
                        if i == 1:
                            value["updated_at"] = conver_value
                        conver_value = value["updated_at"]
                        i += 1

                FileStorage.__objects = tmp
