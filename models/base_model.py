#!/usr/bin/python3
import uuid
from datetime import datetime

"""
This is the module that contains the base class
which defines all common attributes/methods
for other classes.
"""


class BaseModel():
    """ Initi method """
    def __init__(self, *args, **kwargs):
        if len(kwargs) != 0:
            for key in kwargs:
                if key == 'id':
                    self.id = kwargs.get(key)
                if key == 'created_at':
                    self.created_at = datetime.strptime(kwargs.get(key), '%Y-%m-%dT%H:%M:%S.%f')
                if key == 'updated_at':
                    self.updated_at = datetime.strptime(kwargs.get(key), '%Y-%m-%dT%H:%M:%S.%f')
                if key == 'my_number':
                    self.my_number = kwargs.get(key)
                if key == 'name':
                    self.name = kwargs.get(key)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def save(self):
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        basedict = self.__dict__
        basedict['__class__'] = type(self).__name__
        basedict['updated_at'] = self.updated_at.isoformat("T")
        basedict['created_at'] = self.created_at.isoformat("T")
        return basedict

    def __str__(self):
        class_name = type(self).__name__
        id_string = str(self.id)
        return "[" + class_name + "] (" + id_string + ")" + str(self.__dict__)
