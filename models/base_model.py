#!/usr/bin/python3
"""
This is the module that contains the base class which defines all common attributes/methods for other classes.
"""

import uuid, datetime

class BaseModel():
	def __init__(self, id='', created_at='', updated_at=''):
		self.id = str(uuid.uuid4())
		self.created_at = str(datetime.datetime.utcnow().isoformat("T")) 
		self.updated_at = str(datetime.datetime.utcnow().isoformat("T"))


	def save(self):
		self.updated_at = str(datetime.datetime.utcnow())

	def to_dict(self):
		basedict = self.__dict__
		basedict['__class__'] = type(self).__name__
		return basedict

	def __str__(self):
		class_name = type(self).__name__
		id_string = str(self.id)
		return "[" + class_name + "] (" + id_string + str(self.__dict__) + ")"

myObject = BaseModel(1)
print(myObject.__str__())
#print(myObject.to_dict())
