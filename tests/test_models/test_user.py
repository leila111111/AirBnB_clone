"""  unitests for user module"""
import models
import unittest
from models.base_model import BaseModel
from models.user import User
from datetime import datetime
import os


class TestingUser(unittest.TestCase):
    """ testing cases for user class"""

    dicti_attr = {
            "email": "",
            "password": "",
            "first_name": "",
            "last_name": ""
            }

    def test_attr(self):
        """testing attributes"""

        user = User()
        for key, value in TestingUser.dicti_attr.items():
            self.assertTrue(hasattr(user, key))
            self.assertTrue(type(getattr(user, key)), type(value))
        self.assertTrue(type(user.created_at), datetime)

    def test_instant(self):
        """testing instantiation"""

        user1 = User()
        self.assertIsInstance(user1, User)
        self.assertTrue(issubclass(User, User))

    def test_represent(self):
        """test cases for the object representations"""

        user1 = User()
        user1.id = "116"
        date = datetime.now()
        user1.created_at = user1.updated_at = date
        dateRep = repr(date)
        string = str(user1)
        self.assertIn("[User] (116)", string)
        self.assertIn("'created_at': " + dateRep, string)
        self.assertIn("'updated_at': " + dateRep, string)
        self.assertIn("'id': '116'", string)

    def test_toDict(self):
        """test cases for the to_dict method"""

        user3 = User()
        user3.id = "117"
        a = user3.created_at
        b = user3.updated_at
        c = type(user3).__name__
        self.assertEqual(user3.id, user3.to_dict()["id"])
        self.assertEqual(a.isoformat(), user3.to_dict()["created_at"])
        self.assertEqual(b.isoformat(), user3.to_dict()["updated_at"])
        self.assertEqual(c, user3.to_dict()["__class__"])

    def test_save_none(self):
        """ testing save method with None argument"""

        user4 = User()
        with self.assertRaises(TypeError):
            user4.save(None)

    def test_save_updatedattr(self):
        """ testing if updated_at attribute is changed after using
        save method"""

        user5 = User()
        old_updated = user5.updated_at
        user5.save()
        self.assertNotEqual(old_updated, user5.updated_at)

    def test_save_infile(self):
        """ testing if the instance created is saved in the json file after
        the saving method"""

        user6 = User()
        user6.save()
        represen = "User." + user6.id
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
