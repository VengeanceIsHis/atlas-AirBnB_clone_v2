#!/usr/bin/python3
"""This module defines a class to manage the MySQL db for hbnb clone"""


import os
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """This class manages storage of the MySQL DB"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize a DB instance and connects to it"""
        HBNB_MYSQL_USER = os.getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = os.getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = os.getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = os.getenv('HBNB_MYSQL_DB')
        HBNB_ENV = os.getenv('HBNB_ENV')

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                HBNB_MYSQL_USER,
                HBNB_MYSQL_PWD,
                HBNB_MYSQL_HOST,
                HBNB_MYSQL_DB), pool_pre_ping=True)

        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

        self.reload()

    def all(self, cls=None):
        """Query on and return all objects"""
        new_dict = {}
        classes = {
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
            }

        for class_name in classes:
            if cls is None or cls is classes[class_name] or cls is class_name:
                sql_class = classes[class_name]
                objs = self.__session.query(sql_class).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return new_dict

    def new(self, obj):
        """Add a new objet to the current DB"""
        self.__session.add(obj)

    def save(self):
        """Committing changes to the current DB"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete an object from the current DB if it exists"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Creating tables in the DB and initializing the session"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(sess_factory)

    def close(self):
        """Remove the current session and closing it"""
        self.__session.remove()

    def table_dict(self, table_name):
        table_dict = {}
        inspector = inspect(self.__engine)

        # Check if the table exists
        if table_name in inspector.get_table_names():
            sql_class = Base.metadata.tables[table_name]
            objs = self.__session.query(sql_class).all()
            for obj in objs:
                key = obj.__class__.__name__ + '.' + obj.id
                table_dict[key] = obj.__dict__
        else:
            print(f"Table '{table_name}' does not exist.")

        return table_dict