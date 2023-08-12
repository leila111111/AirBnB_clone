#!/usr/bin/python3
"""  unitests for place module"""
import unittest
from models.base_model import BaseModel
from models.place import Place
from datetime import datetime
import os


class TestingPlace(unittest.TestCase):
    """testing cases for place class"""

    def test_attr(self):
        """test attributes"""

        place = Place()
        place.name = "calablanca"
        place.user_id = "115"
        place.amenity_ids = []
        place.city_id = "345"
        place.description = "beautiful place"
        place.number_rooms = 3
        place.number_bathrooms = 4
        place.max_guest = 5
        place.price_by_night = 345
        place.latitude = 345.7585
        place.longitude = 345.876

        self.assertTrue(hasattr(place, "longitude"))
        self.assertTrue(hasattr(place, "user_id"))
        self.assertTrue(hasattr(place, "amenity_ids"))
        self.assertTrue(hasattr(place, "city_id"))
        self.assertTrue(hasattr(place, "name"))
        self.assertTrue(hasattr(place, "description"))
        self.assertTrue(hasattr(place, "number_rooms"))
        self.assertTrue(hasattr(place, "number_bathrooms"))
        self.assertTrue(hasattr(place, "max_guest"))
        self.assertTrue(hasattr(place, "price_by_night"))
        self.assertTrue(hasattr(place, "latitude"))

        self.assertEqual(int, type(place.number_rooms))
        self.assertEqual(float, type(place.longitude))
        self.assertEqual(float, type(place.latitude))
        self.assertEqual(list, type(place.amenity_ids))
        self.assertEqual(str, type(place.city_id))
        self.assertEqual(str, type(place.user_id))
        self.assertEqual(int, type(place.max_guest))
        self.assertEqual(int, type(place.price_by_night))
        self.assertEqual(str, type(place.description))
        self.assertEqual(str, type(place.name))
        self.assertEqual(int, type(place.number_bathrooms))

        self.assertTrue(datetime, type(place.created_at))
        self.assertTrue(datetime, type(place.updated_at))
        self.assertEqual(len(place.__dict__), 14)

    def test_instant(self):
        """testing instantiation"""

        place1 = Place()
        self.assertIsInstance(place1, BaseModel)
        self.assertTrue(issubclass(Place, BaseModel))

    def test_represent(self):
        """test cases for the object representations"""

        place1 = Place()
        place1.id = "116"
        date = datetime.now()
        place1.created_at = place1.updated_at = date
        dateRep = repr(date)
        string = str(place1)
        self.assertIn("[Place] (116)", string)
        self.assertIn("'created_at': " + dateRep, string)
        self.assertIn("'updated_at': " + dateRep, string)
        self.assertIn("'id': '116'", string)

    def test_toDict(self):
        """test cases for the to_dict method"""

        place3 = Place()
        place3.id = "117"
        a = place3.created_at
        b = place3.updated_at
        c = type(place3).__name__
        self.assertEqual(place3.id, place3.to_dict()["id"])
        self.assertEqual(a.isoformat(), place3.to_dict()["created_at"])
        self.assertEqual(b.isoformat(), place3.to_dict()["updated_at"])
        self.assertEqual(c, place3.to_dict()["__class__"])

    def test_save_none(self):
        """testing save method with None argument"""

        place4 = Place()
        with self.assertRaises(TypeError):
            place4.save(None)

    def test_save_updatedattr(self):
        """testing if updated_at attribute is changed after using
        save method"""

        place5 = Place()
        old_updated = place5.updated_at
        place5.save()
        self.assertNotEqual(old_updated, place5.updated_at)

    def test_save_infile(self):
        """testing if the instance created is saved in the json file after
        the saving method"""

        place6 = Place()
        place6.save()
        represen = "Place." + place6.id
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
