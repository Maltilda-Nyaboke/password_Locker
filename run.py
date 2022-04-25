#!/usr/bin/python3.9
from gettext import find
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
    new_credentials = Credentials(site_name,username,password)
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

def display_credentials():
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

def generate_password(ln):
    return Credentials.gen_password(ln)


def main():

    print("Hello welcome to passlock!")

    while True:
        print("Type:\nca-create account\nlg-login\nex-exit")
        short_code = input().lower()
        if short_code == 'ca':
            print("Enter your username")
            print("-"*10)
            username = input("username\n").strip()
            while True:
                    print("Enter password- ep\n use generated one-gp")
                    ent_password = input("select:").lower()
                    if ent_password =='ep':
                        password = input('Enter password\n').strip()
                        break
                    elif ent_password == 'gp':
                        password = Credentials.gen_password(8)
                        print(password)
                        break
                    else: print("Invalid password use the shortcodes option")
            new_user = create_user(username,password)

        elif short_code == 'lg':
            print("Enter your account details to proceed")
            username = input("username: ")
            password = input("password: ")
            user = login(username, password)
            if user == username:
                print(f'welcome {username}')
            else: print("Account not found")
            while True:
                print("Type:\ncc-create credential\n da-display accounts\nfa-locate account\ndel-delete account\nex-exit")
                short_code == input().lower() 
                if short_code == 'cc':
                    print("Enter details to create new account")
                    site_name = input("Account:").strip()
                    username = input("username:").strip()
                    
                    while True:
                        print("Enter password- ep\n use generated one-gp")
                        ent_password = input("select:").lower()
                        if ent_password =='ep':
                          password = input('Enter password\n').strip()
                          break
                        elif ent_password == 'gp':
                            password = Credentials.gen_password(8)
                            break
                        else: print("Invalid password use the shortcodes option")   
                        print(password)
                    
                    save_credentials(create_credentials())
                    print("f{username}of account{site_name}:and password:{password}")
                    
                    

        elif short_code == 'da':

            if display_credentials():
                for credential in display_credentials():
                    print(f"Account:{credential.site_name} -- Username:{credential.username} -- Password:{credential.password}")           
                else:
                    print("There are no saved credentials yet")

        
        elif short_code == 'del':
            print("Enter account you want to delete")
            find = input("Account Name: ").strip()

            if get_credentials(find):
                account = get_credentials(find)
                del_credentials(account)
            else: print("Account does not exist")
        
        
        
        elif short_code == 'ex':
             print("Thanks for visiting1")
             print("-"*10)
             break
            
        else:
            print("Please use shortcodes provided")
        


if __name__ == '__main__':
        main()
