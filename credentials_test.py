from unittest import TestCase, main
from credentials import Credentials
import pyperclip

class TestCredentials(TestCase):
    """
    Defines test cases for the credentials class behaviours.

    Args:
        TestCase: A class that helps create the test cases.
    """

    def setUp(self):
        """
        Method that runs before the test cases.
        """
        self.new_cred = Credentials('github','Lugaga', 'tangodown!')
    def tearDown(self):
        """
        Method that does clean up after each test has run.
        """
        Credentials.cred_list = []
        