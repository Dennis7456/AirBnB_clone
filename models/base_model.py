#!/usr/bin/python3
"""
This is the module that contains the base class
which defines all common attributes/methods
for other classes.
"""

import uuid
from datetime import datetime
from models import storage


class BaseModel():
    """ Defines all common attributes/methods for other classes """
    def __init__(self, *args, **kwargs):
        """ Initializes the instances attributes """
        if kwargs:
            date_format = "%Y-%m-%dT%H:%M:%S.%f"
            k_dict = kwargs.copy()
            del k_dict["__class__"]
            for key in k_dict:
                if (key == "created_at" or key == "updated_at"):
                    k_dict[key] = datetime.strptime(k_dict[key], date_format)
            self.__dict__ = k_dict
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            storage.new(self)

    def save(self):
        """ Save and update instance varriables """
        self.updated_at = datetime.utcnow()
        storage.save()

    def to_dict(self):
         """ Generate a new dict with an extra field __class__ """
         base_dict = self.__dict__.copy()
         base_dict['__class__'] = self.__class__.__name__
         base_dict['created_at'] = self.created_at.isoformat("T")
         base_dict['updated_at'] = self.updated_at.isoformat("T")
         return base_dict

    def __str__(self):
        """ Prints object in reader friendly format"""
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))
    