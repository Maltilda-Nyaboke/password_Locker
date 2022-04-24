
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