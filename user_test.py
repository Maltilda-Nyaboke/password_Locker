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
        '''
        test used to see if user can be saved in the empty user_list
        '''
        self.new_user.save_user() #saving a new user
        self.assertEqual(len(User.user_list),1)

    def test_delete_user(self):
        '''
        test used to see if the user's account can be deleted from the user_list
        '''  
        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1)  


if __name__ == '__main__':
    unittest.main()