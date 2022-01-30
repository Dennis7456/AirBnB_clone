#!/usr/bin/python3
from re import M
from models import storage
from models.base_model import BaseModel

all_objects = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objects:
    obj = all_objects[obj_id]
    print(obj)

print("-- Create a new object --")
my_base_model = BaseModel()
my_base_model.name = "New Model"
my_base_model.my_number = 2222
my_base_model.save()
print(my_base_model)