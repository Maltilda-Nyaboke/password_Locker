
class User:
   '''
   Class user which generates new instances in the user accounts
   '''
   user_list = []
 
   def __init__(self,username,password):
        '''
        use of the __init__method that helps in construction of an object
        Args:
            username = new user username.
            password = new user password.
        '''
        self.username = username
        self.password = password

   def save_user(self):  
        '''
        save_user which is the method used in saving the user contents in the user_list
        
        '''
        User.user_list.append(self) 
    
   def delete_user(self):
       '''
       delete_user is the method used to remove a user from an account
       '''   
       User.user_list.remove(self)  

class Credentials:
     '''
     class that will display the site where the username and password that were used to access it have been stored
     '''  
     credentials_list = [] 

     def __init__(self,site_name, username, password):
          '''
        use of the __init__method that helps in construction of an object
        Args:
            site_name = new user site_name.
            username = new user username.
            password = new user password.
        '''    
          self.site_name = site_name
          self.username = username
          self.password = password

     def save_credentials(self):
          '''
          This method will save the credentials in the credentials_list
          '''  
          Credentials.credentials_list.append(self)   