#!/usr/bin/python3
"""
City class for new cities
"""
from models.base_model import BaseModel

class City(BaseModel):
    """ City class extends BaseModel"""
    state_id = ""
    name = ""