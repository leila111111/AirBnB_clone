#!/usr/bin/python3
"""  unitests for amenity module"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
from datetime import datetime
import os


class TestingAmenity(unittest.TestCase):
    """testing cases for amenity class"""

    def test_attr(self):
        """test attributes"""

        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))
        self.assertIsInstance(amenity.created_at, datetime)
        self.assertIsInstance(amenity.updated_at, datetime)
        self.assertIsInstance(amenity.id, str)
        self.assertIsInstance(amenity.name, str)

    def test_instant(self):
        """testing instantiation"""

        amenity1 = Amenity()
        self.assertIsInstance(amenity1, BaseModel)
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_represent(self):
        """test cases for the object representations"""

        amenity1 = Amenity()
        amenity1.id = "116"
        date = datetime.now()
        amenity1.created_at = amenity1.updated_at = date
        dateRep = repr(date)
        string = str(amenity1)
        self.assertIn("[Amenity] (116)", string)
        self.assertIn("'created_at': " + dateRep, string)
        self.assertIn("'updated_at': " + dateRep, string)
        self.assertIn("'id': '116'", string)

    def test_toDict(self):
        """test cases for the to_dict method"""

        amenity3 = Amenity()
        amenity3.id = "117"
        a = amenity3.created_at
        b = amenity3.updated_at
        c = type(amenity3).__name__
        self.assertEqual(amenity3.id, amenity3.to_dict()["id"])
        self.assertEqual(a.isoformat(), amenity3.to_dict()["created_at"])
        self.assertEqual(b.isoformat(), amenity3.to_dict()["updated_at"])
        self.assertEqual(c, amenity3.to_dict()["__class__"])

    def test_save_none(self):
        """testing save method with None argument"""

        amenity4 = Amenity()
        with self.assertRaises(TypeError):
            amenity4.save(None)

    def test_save_updatedattr(self):
        """testing if updated_at attribute is changed after using
        save method"""

        amenity5 = Amenity()
        old_updated = amenity5.updated_at
        amenity5.save()
        self.assertNotEqual(old_updated, amenity5.updated_at)

    def test_save_infile(self):
        """testing if the instance created is saved in the json file after
        the saving method"""

        amenity6 = Amenity()
        amenity6.save()
        represen = "Amenity." + amenity6.id
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
