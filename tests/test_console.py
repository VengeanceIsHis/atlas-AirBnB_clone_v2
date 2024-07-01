#!/usr/bin/python3
"""Module for testing for console"""


from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import unittest
from console import HBNBCommand
import sys
from io import StringIO


class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()
        self.stdout = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
        sys.stdout = self.stdout

    def test_prompt(self):
        self.assertEqual(self.console.prompt, '(hbnb) ')

    def test_create_state(self):
        """Test creating a new State"""
        new_state = State(name="California")
        new_state.save()
        self.storage.save()

        key = "State.{}".format(new_state.id)
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key].name, "California")


if __name__ == "__main__":
    unittest.main()
