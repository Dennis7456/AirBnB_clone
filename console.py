#!/usr/bin/python3
import cmd
from shlex import shlex
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage
"""This is the console module which contains the HBNB class
which is the main entry point for the console"""

my_class = {"BaseModel": BaseModel}

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'
    file = None #maybe remove

    def do_quit(self, arg):
        """ Command to quit the program"""
        return True

    def do_EOF(self, arg):
        """ Command to exit the program"""
        return True

    def emptyline(self):
        """ Command to prevent execution in case of an empty line"""
        pass

    def do_create(self, arg):
        """ Command to create a new instance of a class """
        if not arg:
            print("** class name missing **")
        elif arg in my_class:
            for key, value in my_class.items():
                if key == arg:
                    new_instance = my_class[key]()
            storage.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """ Command to show an instance of an existing class """
        my_arg = arg.split(" ")
        if not arg:
            print("** class name missing **")
        elif my_arg[0] not in my_class:
            print("** class doesn't exist **")
        elif len(my_arg) >= 1:
            try:
                my_objects = FileStorage.all(self)
                my_key = my_arg[0] + "." + my_arg[1]
                flag = 0
                for key, value in my_objects:
                    if key == my_key:
                        flag = 1
                        print(value)
                if flag == 0:
                    print("** instance id missing **")
            except:
                print("** no instance found **")
    def do_destroy(self, arg):
        """ command to delete an instance of an object """
        my_arg = arg.split(" ")
        if not arg:
            print("** class name missing **")
        elif my_arg[0] not in my_class:
            print("** class doesn't exist **")
        elif len(my_arg) >= 1:
            try:
                my_objects = FileStorage.all(self)
                my_key = my_arg[0] + "." + my_arg[1]
                my_objects.pop(my_key)
                storage.save()
            except KeyError:
                print("** no instance found **")
            except IndexError:
                print("** instance id missing **")
        
    def do_all(self, arg):
        """ Command to display all objects with or without the class name """
        my_arg = arg.split(" ")
        if not arg:
            my_list = []
            my_objects = FileStorage.all(self)
            for key, value in my_objects.items():
                my_list.append(str(value))
            print(my_list)
        elif my_arg[0] not in my_class:
            print("** class doesn't exist **")
        else:
            my_list = []
            my_objects = FileStorage.all(self)
            for key, value in my_objects.items():
                my_key = key.split(".")
                if my_key[0] == my_arg[0]:
                    my_list.append(str(value))
            print(my_list)
    
    def do_update(self, arg):
        """ Command to update an instance based on class name and id"""
        my_arg = shlex.split(arg)
        if len(my_arg) == 0:
            print("** class name missing **")
        elif len(my_arg) == 1:
            print("** instance id missing **")
        elif len(my_arg) == 2:
            print("** attribute name missing **")
        elif len(my_arg) == 3:
            print("** value missing **")
        elif my_arg[0] not in my_class:
            print("** class doesn't exist **")
        else:
            my_objects = FileStorage.all(self)
            my_key = my_arg[0] + "." + my_arg[1]
            flag = 0
            for key, value in my_objects.items():
                if key == my_key:
                    flag = 1
                    my_values = my_objects.get(key)
                    setattr(value, my_arg[2], my_arg[3])
                    value.save()
            if flag == 0:
                print("** no instance found **")
if __name__ == "__main__":
    HBNBCommand().cmdloop()
