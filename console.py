#!/usr/bin/python3
""" The Console """
import cmd
import uuid
import datetime
from models import storage

class HBNBCommand(cmd.Cmd):
    """ The Airbnb Project Console."""
    prompt = '(hbnb) '

    def do_greet(self, line):
        print ("hello")

    def do_EOF(self, line):
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
