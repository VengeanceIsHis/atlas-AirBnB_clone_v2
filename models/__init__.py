#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""


from models.engine.file_storage import FileStorage
import os

storage_selection = os.getenv('HBNB_TYPE_STORAGE', 'file')

if storage_selection == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
