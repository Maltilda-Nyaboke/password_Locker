import unittest
from user import User

class TestUser(unittest.TestCase):
    
    '''
    Test class that defines test cases for user class behaviours.

    Args:
        unittest.Testcase:Testcase class that helps in creating test cases
    '''

    def setUp(self):
   
        '''
        set up method to run before each test case
        ''' 
        
        self.new_user= User("Tilda","Welcome!")   

    def test_init(self):
        '''
        test_init test case to see if the object is initialized properly
        '''
        self.assertEqual(self.new_user.username,"Tilda")
        self.assertEqual(self.new_user.password,"Welcome!")

    def test_save_user(self):
        
if __name__ == '__main__':
    unittest.main()