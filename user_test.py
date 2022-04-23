import unittest
from user import User

class TestUser(unittest.TestCase):
    '''
    class Test that defines test cases for user class behaviours.

    Args:
        unittest.Testcase:Testcase class that helps in creating test cases
    '''
def setUp(self):
    '''
    set up method to run before each test case
    ''' 
    self.new_user= User("Tilda","Welcome!")   