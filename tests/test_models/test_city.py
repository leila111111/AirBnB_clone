#!/usr/bin/python3
"""  unitests for city module"""
import unittest
from models.base_model import BaseModel
from models.city import City
from datetime import datetime
import os


class TestingCity(unittest.TestCase):
    """testing cases for city class"""

    def test_attr(self):
        """test attributes"""

        city = City()
        city.name = "NewYork"
        city.id = "115"
        self.assertTrue(hasattr(city, "name"))
        self.assertTrue(hasattr(city, "id"))
        self.assertEqual(str, type(city.id))
        self.assertEqual(str, type(city.name))
        self.assertTrue(datetime, type(city.created_at))
        self.assertTrue(datetime, type(city.updated_at))
        self.assertEqual(len(city.__dict__), 4)

    def test_instant(self):
        """testing instantiation"""

        city1 = City()
        self.assertIsInstance(city1, BaseModel)
        self.assertTrue(issubclass(City, BaseModel))

    def test_represent(self):
        """test cases for the object representations"""

        city1 = City()
        city1.id = "116"
        date = datetime.now()
        city1.created_at = city1.updated_at = date
        dateRep = repr(date)
        string = str(city1)
        self.assertIn("[City] (116)", string)
        self.assertIn("'created_at': " + dateRep, string)
        self.assertIn("'updated_at': " + dateRep, string)
        self.assertIn("'id': '116'", string)

    def test_toDict(self):
        """test cases for the to_dict method"""

        city3 = City()
        city3.id = "117"
        a = city3.created_at
        b = city3.updated_at
        c = type(city3).__name__
        self.assertEqual(city3.id, city3.to_dict()["id"])
        self.assertEqual(a.isoformat(), city3.to_dict()["created_at"])
        self.assertEqual(b.isoformat(), city3.to_dict()["updated_at"])
        self.assertEqual(c, city3.to_dict()["__class__"])

    def test_save_none(self):
        """testing save method with None argument"""

        city4 = City()
        with self.assertRaises(TypeError):
            city4.save(None)

    def test_save_updatedattr(self):
        """testing if updated_at attribute is changed after using
        save method"""

        city5 = City()
        old_updated = city5.updated_at
        city5.save()
        self.assertNotEqual(old_updated, city5.updated_at)

    def test_save_infile(self):
        """testing if the instance created is saved in the json file after
        the saving method"""

        city6 = City()
        city6.save()
        represen = "City." + city6.id
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
