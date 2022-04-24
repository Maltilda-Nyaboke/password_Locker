#!/usr/bin/env python3.9
from user import User,Credentials

def main():
    pass

def create_user(username, password):
    '''
    Create a new user
    '''
    new_user = User(username, password)
    return new_user

def save_user(user):
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
    credentials.delete_user()

def display_credentials(credentials):
    '''
    function to display credentials
    ''' 
    return Credentials.display_credentials()   

def get_credentials(name):
    '''
    function to retrieve credentials
    '''  
    return Credentials.get_credentials(name)  


    if __name__ == '__main__':
        main()
