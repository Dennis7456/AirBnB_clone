#!/usr/bin/python3

""" Review class for new reviews """

from models.base_model import BaseModel


class Review(BaseModel):
    """ Review subclass inherits from BaseModel """
    place_id = ""
    user_id = ""
    text = ""
