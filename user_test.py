import unittest
from user import User
from user import Credentials
import pyperclip

class TestUser(unittest.TestCase):
    
    '''
    Test class that defines test cases for user class behaviours.

     Args:
    unittest.Testcase:Testcase class that helps in creating test cases
    '''
                # First test case
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
                
                # Second test case
    
    def test_save_user(self):
        '''
        test used to see if user can be saved in the empty user_list
        '''
        self.new_user.save_user() #saving a new user
        self.assertEqual(len(User.user_list),2)
       
                     # Third test case
    
    def test_delete_user(self):
        '''
        test used to see if the user's account can be deleted from the user_list
        '''  
        self.new_user.save_user()
        test_user = User("Tilda", "Welcome!")
        test_user.save_user()
        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1)  


class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for credentials class behaviours.

    '''
    
     # First test case-cred
    
    def setUp(self):
        '''
        initializing the credentials class
        '''
        self.new_credentials = Credentials("twitter", "Tilda", "Welcome!") 
    def test_init(self):
        '''
        test_init test case to see if the object is initialized properly
        '''
        self.assertEqual(self.new_credentials.site_name,"twitter")
        self.assertEqual(self.new_credentials.username,"Tilda")
        self.assertEqual(self.new_credentials.password,"Welcome!")
         
                # Second test case-cred
    
    def test_save_credentials(self):
            '''
            test used to save credentials
            '''
            self.new_credentials.save_credentials()
            self.assertEqual(len(Credentials.credentials_list),2)    
             
                # Third test case-cred
    
    def test_delete_credentials(self):
            '''
            test used to delete the stored credentials
            '''
            self.new_credentials.save_credentials()
            test_credentials = Credentials("twitter","Tilda","Welcome!")
            test_credentials.save_credentials()
            self.new_credentials.delete_credentials()
            self.assertEqual(len(Credentials.credentials_list),1)    
                   
                    # Fourth test case-cred
    
    def test_display_all_credentials(self):
            '''
            test used to dispaly all the credential lists stored in the list
            '''
            self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)



if __name__ == '__main__':
    unittest.main()