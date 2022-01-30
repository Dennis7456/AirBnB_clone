#!/usr/bin/python3
import json

""" Class for filestorage """
class FileStorage():
    def __init__(self, file_path='my_storagefile.json', objects={}):
        self.__file_path = file_path
        self.__objects = objects

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[obj.id] = obj
        return self.__objects

    def save(self):
        new_dict = {}
        for key, value in self.__objects.items():
            print("Save {} as key and {} as value".format(key, value))
            new_dict.update({key: value.to_dict()})
        json_file = json.dumps(new_dict)
        with open(self.__file_path, "w") as my_file:
            my_file.write(json_file)

    
    def reload(self):
        try: 
            return json.load(self.__file_path)
        except:
            pass


