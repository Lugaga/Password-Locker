from unittest import TestCase
from user import User


class TestUser(TestCase):
    """
      Defines test cases for the user class behaviours.

      Args:
        TestCase: A class that helps create the test cases.
    """

    def setUp(self):
        """
        Method to run before the test cases.
        """
        self.new_user = User('Lugaga', 'Maurice', 'Lugaga', 'Tangodown!')

    def test_init(self):
        """
        Test case to see if the object is being initialized properly.
        """
        self.assertEqual(self.new_user.first_name, 'Lugaga')
        self.assertEqual(self.new_user.last_name, 'Maurice')
        self.assertEqual(self.new_user.username, 'Lugaga')
        self.assertEqual(self.new_user.password, 'TangoDown!')

if __name__ == '__main__':
    main()
