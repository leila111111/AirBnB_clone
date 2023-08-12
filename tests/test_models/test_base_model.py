#!/usr/bin/python3
"""  test for base_model module"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
import models


class Testbasemodel(unittest.TestCase):
    """class created to do test cases
    for base_model module"""

    def test_attr(self):
        """test attributes"""

        model = BaseModel()
        model.name = "model"
        model.id = "115"
        self.assertTrue(hasattr(model, "name"))
        self.assertTrue(hasattr(model, "id"))
        self.assertEqual(str, type(model.id))
        self.assertEqual(str, type(model.name))
        self.assertTrue(datetime, type(model.created_at))
        self.assertTrue(datetime, type(model.updated_at))
        self.assertEqual(len(model.__dict__), 4)

    def test_represent(self):
        """test cases for the object representations"""

        model1 = BaseModel()
        model1.id = "116"
        date = datetime.now()
        model1.created_at = model1.updated_at = date
        dateRep = repr(date)
        string = str(model1)
        self.assertIn("[BaseModel] (116)", string)
        self.assertIn("'created_at': " + dateRep, string)
        self.assertIn("'updated_at': " + dateRep, string)
        self.assertIn("'id': '116'", string)

    def test_toDict(self):
        """test cases for the to_dict method"""

        model3 = BaseModel()
        model3.id = "117"
        a = model3.created_at
        b = model3.updated_at
        c = type(model3).__name__
        self.assertEqual(model3.id, model3.to_dict()["id"])
        self.assertEqual(a.isoformat(), model3.to_dict()["created_at"])
        self.assertEqual(b.isoformat(), model3.to_dict()["updated_at"])
        self.assertEqual(c, model3.to_dict()["__class__"])

    def test_instant(self):
        """testing instantiation"""

        model2 = BaseModel()
        self.assertIsInstance(model2, BaseModel)


if __name__ == "__main__":
    unittest.main()
