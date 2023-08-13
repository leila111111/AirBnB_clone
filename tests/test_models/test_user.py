#!/usr/bin/python3
""" unitests for user module """
import unittest
from models.user import User
from datetime import datetime


class TestUser(unittest.TestCase):
    """testing cases for user class"""

    def test_userattr(self):
        """test attributes"""
        us = User()
        self.assertTrue(hasattr(us, "id"))
        self.assertTrue(hasattr(us, "created_at"))
        self.assertTrue(hasattr(us, "updated_at"))
        self.assertTrue(hasattr(us, "email"))
        self.assertTrue(hasattr(us, "password"))
        self.assertTrue(hasattr(us, "first_name"))
        self.assertTrue(hasattr(us, "last_name"))

        """test the type of attributes"""
        self.assertIsInstance(us.id, str)
        self.assertIsInstance(us.created_at, datetime)
        self.assertIsInstance(us.updated_at, datetime)
        self.assertIsInstance(us.email, str)
        self.assertIsInstance(us.password, str)
        self.assertIsInstance(us.first_name, str)
        self.assertIsInstance(us.last_name, str)


if __name__ == "__main__":
    unittest.main()
