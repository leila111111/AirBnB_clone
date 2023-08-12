"""  unitests for user module"""
import models
import unittest
from models.base_model import BaseModel
from models.user import User
from datetime import datetime


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
        self.assertIsInstance(user1, BaseModel)
        self.assertTrue(issubclass(User, BaseModel))


if __name__ == "__main__":
    unittest.main()
