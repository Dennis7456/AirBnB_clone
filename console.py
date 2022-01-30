#!/usr/bin/python3
import cmd
"""This is the console module which contains the HBNB class
which is the main entry point for the console"""

class HBNBCommand(cmd.Cmd):
    def do_quit(self, arg):
        """ Command to quit the program"""
        return True
    def do_EOF(self, arg):
        """ Command to exit the program"""
        return True
    def emptyline(self):
        """ Command to prevent execution in case of an empty line"""
        pass
if __name__ == "__main__":
    HBNBCommand().cmdloop()