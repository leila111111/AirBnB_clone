#!/usr/bin/python3
"""  unitests for state module"""
import models
import unittest
from models.base_model import BaseModel
from models.state import State
from datetime import datetime
import os


class TestingState(unittest.TestCase):
    """testing cases for state class"""

    def test_attr(self):
        """test attributes"""

        state = State()
        state.name = "NewYork"
        state.id = "115"
        self.assertTrue(hasattr(state, "name"))
        self.assertTrue(hasattr(state, "id"))
        self.assertEqual(str, type(state.id))
        self.assertEqual(str, type(state.name))
        self.assertTrue(datetime, type(state.created_at))
        self.assertTrue(datetime, type(state.updated_at))
        self.assertEqual(len(state.__dict__), 4)

    def test_instant(self):
        """testing instantiation"""

        state1 = State()
        self.assertIsInstance(state1, BaseModel)
        self.assertTrue(issubclass(State, BaseModel))

    def test_represent(self):
        """test cases for the object representations"""

        state1 = State()
        state1.id = "116"
        date = datetime.now()
        state1.created_at = state1.updated_at = date
        dateRep = repr(date)
        string = str(state1)
        self.assertIn("[State] (116)", string)
        self.assertIn("'created_at': " + dateRep, string)
        self.assertIn("'updated_at': " + dateRep, string)
        self.assertIn("'id': '116'", string)

    def test_toDict(self):
        """test cases for the to_dict method"""

        state3 = State()
        state3.id = "117"
        a = state3.created_at
        b = state3.updated_at
        c = type(state3).__name__
        self.assertEqual(state3.id, state3.to_dict()["id"])
        self.assertEqual(a.isoformat(), state3.to_dict()["created_at"])
        self.assertEqual(b.isoformat(), state3.to_dict()["updated_at"])
        self.assertEqual(c, state3.to_dict()["__class__"])

    def test_save_none(self):
        """testing save method with None argument"""

        state4 = State()
        with self.assertRaises(TypeError):
            state4.save(None)

    def test_save_updatedattr(self):
        """testing if updated_at attribute is changed after using
        save method"""

        state5 = State()
        old_updated = state5.updated_at
        state5.save()
        self.assertNotEqual(old_updated, state5.updated_at)

    def test_save_infile(self):
        """testing if the instance created is saved in the json file after
        the saving method"""

        state6 = State()
        state6.save()
        represen = "State." + state6.id
        with open("file.json", "r") as file:
            self.assertIn(represen, file.read())

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "temp.json")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("temp.json", "file.json")
        except IOError:
            pass


if __name__ == "__main__":
    unittest.main()
