#!/usr/bin/python3
from turtle import st
import uuid
from datetime import datetime
from models.__init__ import storage

"""
This is the module that contains the base class
which defines all common attributes/methods
for other classes.
"""


class BaseModel():
    """ Init method """
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
            storage.new(self)

    def save(self):
        self.updated_at = datetime.utcnow()
        storage.save()

    def to_dict(self):
        basedict = self.__dict__
        basedict['__class__'] = self.__class__.__name__
        basedict['created_at'] = self.created_at.isoformat("T")
        basedict['updated_at'] = self.updated_at.isoformat("T")
        return basedict

    def __str__(self):
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))
