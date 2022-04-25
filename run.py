#!/usr/bin/python3.9
from user import User,Credentials

def main():
    pass

def create_user(username,password):
    '''
    Create a new user
    '''
    new_user = User(username,password)
    return new_user

def sav_user(user):
    '''
    function to save the user
    '''
    user.save_user()

def del_user(user):
    '''
    function to delete a user
    '''
    user.delete_user()

def create_credentials(site_name,username, password):
    '''
    Create  new user"s credentials
    '''
    new_credentials = Credentials(site_name,username, password)
    return new_credentials

def save_credentials(credentials):
    '''
    function to save the user credentials
    '''
    credentials.save_credentials()

def del_credentials(credentials):
    '''
    function to delete site credentials
    '''
    credentials.delete_credentials()

def display_credentials(credentials):
    '''
    function to display credentials
    ''' 
    return Credentials.display_credentials()   

def get_credentials(name):
    '''
    function to retrieve credentials
    '''  
    return Credentials.find_credentials(name)  

def login(username, password):
    return Credentials.verify_user(username, password) 

def main():

    print("Hello welcome to")

    while True:
        print("Use these shortcodes to access your account:ca-create account, lg-login,da-display accounts,fa-locate your account,ex-exit")
        short_code = input().lower()
        if short_code == 'ca':
            print("Enter your username")
            print("-"*10)
            username = input("username\n").strip()
            while True:
                    print("Enter password('ep')\n use generated one")
                    ent_password = input("Choice:").lower()
                    if ent_password =='ep':
                        password = input('Enter password\n').strip()
                        break
                    elif ent_password == 'gp':
                        password = input('Generate password').strip()
        elif short_code == 'da':
            if display_credentials():
                print("Here is a list of all your accounts")
                print("\n")
                

                for credential in display_credentials():
                    print(f"(Account:credential.site_name,username, password)")




if __name__ == '__main__':
        main()
