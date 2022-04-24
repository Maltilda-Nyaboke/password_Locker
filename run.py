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

def get_user(user)    


    if __name__ == '__main__':
        main()
