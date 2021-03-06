#!/usr/bin/python3
"""This is the console module which contains the HBNB class
which is the main entry point for the console"""

import cmd
import shlex
from models.base_model import BaseModel
from models import storage
import json
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):

    """ Airbnb Clone command prompt to access model data """

    prompt = '(hbnb)'
    my_dict = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

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
        """ Command to create a new instance of a class
        Usage: create <class name>"""
        if not arg:
            print("** class name missing **")
            return
        tokens = shlex.split(arg)
        if tokens[0] not in HBNBCommand.my_dict.keys():
            print("** class doesn't exist**")
            return
        new_instance = HBNBCommand.my_dict[tokens[0]]()
        new_instance.save()

    def do_show(self, arg):
        """ Command to show an instance of an existing class
        based on the class name and id
        Usage: show <class name> <id>"""
        tokens = shlex.split(arg)
        if len(tokens) == 0:
            print("** class name missing **")
            return
        if tokens[0] not in HBNBCommand.my_dict.keys():
            print("** class doesn't exist **")
            return
        if len(tokens) <= 1:
            print("** instance id missing **")
            return
        storage.reload()
        objects_dict = storage.all()
        key = tokens[0] + "." + tokens[1]
        if key in objects_dict:
            object_instance = str(objects_dict[key])
            print(object_instance)
        else:
            print("** instance not found**")

    def do_destroy(self, arg):
        """ command to delete an instance of an object
        and save the changes to the JSON file
        Usage: destroy <class name> <id>"""

        tokens = shlex.split(arg)
        if len(tokens) == 0:
            print("** class name missing **")
            return
        if tokens[0] not in HBNBCommand.my_dict.keys():
            print("** class doesn't exist **")
            return
        if len(tokens) <= 1:
            print("** instance id missing **")
            return
        storage.reload()
        objs_dict = storage.all()
        key = tokens[0] + "." + tokens[1]
        if key in objs_dict:
            del objs_dict[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name
        Usage: all <class name> or all
        """
        # prints the whole file
        storage.reload()
        my_json = []
        objects_dict = storage.all()
        if not arg:
            for key in objects_dict:
                my_json.append(str(objects_dict[key]))
            print(json.dumps(my_json))
            return
        token = shlex.split(arg)
        if token[0] in HBNBCommand.my_dict.keys():
            for key in objects_dict:
                if token[0] in key:
                    my_json.append(str(objects_dict[key]))
            print(json.dumps(my_json))
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Updates an instance based on the class name and
        id by adding or updating attribute
        (save the change into the JSON file).
        Usage: <class name> <id> <arg name> <arg value>
        """
        if not arg:
            print("** class name missing **")
            return
        my_data = shlex.split(arg)
        storage.reload()
        objs_dict = storage.all()
        if my_data[0] not in HBNBCommand.my_dict.keys():
            print("** class doesn't exist **")
            return
        if (len(my_data) == 1):
            print("** instance id missing **")
            return
        try:
            key = my_data[0] + "." + my_data[1]
            objs_dict[key]
        except KeyError:
            print("** no instance found **")
            return
        if (len(my_data) == 2):
            print("** attribute name missing **")
            return
        if (len(my_data) == 3):
            print("** value missing **")
            return
        my_instance = objs_dict[key]
        if hasattr(my_instance, my_data[2]):
            data_type = type(getattr(my_instance, my_data[2]))
            setattr(my_instance, my_data[2], data_type(my_data[3]))
        else:
            setattr(my_instance, my_data[2], my_data[3])
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
