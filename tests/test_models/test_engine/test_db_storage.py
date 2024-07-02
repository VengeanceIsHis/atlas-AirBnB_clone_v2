#!/usr/bin/python3
"""Unit tests for DBStorage class"""


import unittest
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base_model import Base
from models.state import State
from models.city import City


class TestDBStorage(unittest.TestCase):
    """Test for DBStorage class"""
    
    @classmethod
    def setUpClass(cls):
        """Set up the test database engine and session."""
        os.environ['HBNB_ENV'] = 'test'
        os.environ['HBNB_MYSQL_USER'] = 'hbnb_dev'
        os.environ['HBNB_MYSQL_PWD'] = 'hbnb_dev_pwd'
        os.environ['HBNB_MYSQL_HOST'] = 'localhost'
        os.environ['HBNB_MYSQL_DB'] = 'hbnb_dev_db'

        cls.engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                os.getenv('HBNB_MYSQL_USER'),
                os.getenv('HBNB_MYSQL_PWD'),
                os.getenv('HBNB_MYSQL_HOST'),
                os.getenv('HBNB_MYSQL_DB')), pool_pre_ping=True)
        Base.metadata.create_all(cls.engine)
        cls.Session = sessionmaker(bind=cls.engine)

    @classmethod
    def tearDownClass(cls):
        """Teardown the test database."""
        Base.metadata.drop_all(cls.engine)

    def setUp(self):
        """Create a new session for each test."""
        self.session = self.Session()

    def tearDown(self):
        """Cleanup after each test."""
        self.session.close()

    def test_state_create(self):
        """Test creating and saving a State object."""
        state = State(name='California')
        self.session.add(state)
        self.session.commit()
        self.assertIn(state, self.session)

    def test_city_create(self):
        """Test creating and saving a City object."""
        state = State(name='California')
        city = City(name='San Francisco', state_id=state.id)
        self.session.add(state)
        self.session.add(city)
        self.session.commit()
        self.assertIn(city, self.session)


if __name__ == '__main__':
    unittest.main()
