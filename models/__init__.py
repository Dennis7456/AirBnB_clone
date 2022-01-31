#!/usr/bin/python3
""" call to storage class """

from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
