#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
print("-- Base Model --")
print(my_model.id)
print(my_model)