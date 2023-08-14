#!/usr/bin/python3
"""  unitests for review module"""
import unittest
from models.base_model import BaseModel
from models.review import Review
from datetime import datetime
import os


class TestingReview(unittest.TestCase):
    """testing cases for review class"""

    def test_attr(self):
        """test attributes"""

        review = Review()
        self.assertTrue(hasattr(review, "user_id"))
        self.assertTrue(hasattr(review, "place_id"))
        self.assertTrue(hasattr(review, "text"))
        self.assertTrue(hasattr(review, "id"))
        self.assertTrue(hasattr(review, "created_at"))
        self.assertTrue(hasattr(review, "updated_at"))
        self.assertIsInstance(review.user_id, str)
        self.assertIsInstance(review.text, str)
        self.assertIsInstance(review.id, str)
        self.assertIsInstance(review.place_id, str)
        self.assertIsInstance(review.created_at, datetime)
        self.assertIsInstance(review.updated_at, datetime)

    def test_instant(self):
        """testing instantiation"""

        review1 = Review()
        self.assertIsInstance(review1, BaseModel)
        self.assertTrue(issubclass(Review, BaseModel))

    def test_represent(self):
        """test cases for the object representations"""

        review1 = Review()
        review1.id = "116"
        date = datetime.now()
        review1.created_at = review1.updated_at = date
        dateRep = repr(date)
        string = str(review1)
        self.assertIn("[Review] (116)", string)
        self.assertIn("'created_at': " + dateRep, string)
        self.assertIn("'updated_at': " + dateRep, string)
        self.assertIn("'id': '116'", string)

    def test_toDict(self):
        """test cases for the to_dict method"""

        review3 = Review()
        review3.id = "117"
        a = review3.created_at
        b = review3.updated_at
        c = type(review3).__name__
        self.assertEqual(review3.id, review3.to_dict()["id"])
        self.assertEqual(a.isoformat(), review3.to_dict()["created_at"])
        self.assertEqual(b.isoformat(), review3.to_dict()["updated_at"])
        self.assertEqual(c, review3.to_dict()["__class__"])

    def test_save_none(self):
        """testing save method with None argument"""

        review4 = Review()
        with self.assertRaises(TypeError):
            review4.save(None)

    def test_save_updatedattr(self):
        """testing if updated_at attribute is changed after using
        save method"""

        review5 = Review()
        old_updated = review5.updated_at
        review5.save()
        self.assertNotEqual(old_updated, review5.updated_at)

    def test_save_infile(self):
        """testing if the instance created is saved in the json file after
        the saving method"""

        review6 = Review()
        review6.save()
        represen = "Review." + review6.id
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
