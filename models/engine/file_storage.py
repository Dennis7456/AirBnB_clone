#!/usr/bin/python3
import json

from models.base_model import BaseModel
from models.user import User

""" Class for filestorage """
class FileStorage():

    __file_path = 'my_storagefile.json'
    __objects = {}

    def __init__(self):
        self.reload()

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        new_dict = {}
        current_dict = FileStorage.__objects
        print("This is the current dict {}".format(current_dict))
        for key, value in current_dict.items():
            print("Key: {}".format(key))
            print("Value: {}".format(value))
            try:
                new_dict.update({key: value.to_dict()})
            except:
                pass
        json_file = json.dumps(new_dict)
        with open(FileStorage.__file_path, "w") as my_file:
            my_file.write(json_file)

    
    def reload(self):
        my_dict = {"BaseModel": BaseModel, "User": User}
        json_file = ""
        try:
            if FileStorage.__file_path:
                with open(FileStorage.__file_path, "r", encoding="UTF8") as my_file:
                    json_file = my_file.read()
                    for key, value in json_file.items():
                        FileStorage.__objects[key] = my_dict[json_file[key]['__class__']](**json_file[key])

        except:
            pass

