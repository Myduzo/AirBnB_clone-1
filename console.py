#!/usr/bin/python3
""" The Console """
import cmd
import uuid
import datetime
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ The Airbnb Project Console."""
    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        pass

    def do_create(self, l):
        """Creates a New instance of a given class"""
        line = l.split()
        if len(line) == 0:
            print ("** class name missing **")
        elif line[0] == "BaseModel":
            z = BaseModel()
            z.save()
            print(z.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, l):
        line = l.split()
        if len(line) == 0:
            print("** class name missing **")
        elif line[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(line) == 1:
            print ("** instance id missing **")
        elif len(line) == 2:
            dt = {}
            for key, value in storage.all().items():
                if line[1] in key and line[0] in key:
                    dt[key] = value
            if len(dt) == 0:
                print("** no instance found **")
            else:
                print("[{}] ({}) {}".format(
                    line[0], line[1], dt[line[0] + "." + line[1]]
                ))
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
