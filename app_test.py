import unittest
from app import *

class TestApp(unittest.TestCase):

    def test_user_firstname(self):
        #arrange
        username = "Peter"
        #act
        checkResult = verifyUserFirstName(username)
        #assert
        self.assertEqual(username, "Peter")

    def test_with_error(self):
        #arrange
        username = 123
        #act
        verifyResult = verifyUserFirstName(username)
        #assert
        self.assertEqual(username, "Test")

    def test_user_age(self):
        #arrange
        age = 30
        #act
        verifyResult = verifyAge(age)
        #assert
        self.assertEqual(age, 30)

    def test_user_age(self):
        #arrange
        age = "string"
        #act
        verifyResult = verifyAge(age)
        #assert
        self.assertEqual(age, 30)