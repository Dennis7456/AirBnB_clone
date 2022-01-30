#!/usr/bin/python3
from models.base_model import BaseModel

""" Amenity class """
class Amenity(BaseModel):
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
