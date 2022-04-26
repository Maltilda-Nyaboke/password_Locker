#! /usr/bin/env python3

from users import User
from credentials import Credentials


def create_user(name, username, password):
    """
    Function that create a new user account
    """
    new_user = User(name, username, password)
    return new_user


def save_user(user):
    User.save_user_account(user)


def verify_saved_user(username, password):
    """
    Function that checks whether the user account exists
    """
    checking_user = User.check_user(username, password)
    return checking_user


def generate_password(ln):
    """
    Function to generate a password automatically
    """
    gen_pass = Credentials.gen_password(ln)
    return gen_pass


def create_credentials(platform_name, username, password):
    """
    Function to create a new credential
    """
    new_credential = Credentials(platform_name, username, password)
    return new_credential


def save_credentials(credential):
    """
    Function to save a newly created credential
    """
    return Credentials.save_credentials(credential)


def delete_credentials(credential):
    """Function to delete a previously created credential"""
    return credential.delete_credentials()


def search_credentials(platform_name):
    """
    Function to search for a credential
    """
    return Credentials.search_credentials(platform_name)


def display_credentials(platform_name):
    """
    Function to display credentials saved by a user on request
    """
    return Credentials.display_credentials(platform_name)


def copy_credentials(platform_name):
    """
    Function to copy a credentials details to the clipboard
    """
    return Credentials.copy_credentials(platform_name)

def password_locker():
    print("Welcome to Password Locker.")
    while True:
        print("-" * 60)
        print(
            "Select an option: \n 11-Create your password Locker Account \n 22-Log In \n 33-Exit Password Locker")
        short_code = input("Enter option: ").lower().strip()
        if short_code == "33":
            break

        elif short_code == "11":
            print("-" * 60)

            print("creating a new password locker account:")
            name = input("Enter your name: \t").strip()
            username = input("Enter your preferred username: \t").strip()
            password = input("password: \t").strip()
            save_user(create_user(name, username, password))

            print(
                f"New Account Created for: {name} Username: {username} and password: {password} successfully created")
        elif short_code == "22":
            print("-" * 60)

            print("Enter your details to log in:")
            username = input(" Username: ").strip()
            password = input(" Password: ").strip()
            if_user_exist = verify_saved_user(username, password)
            if if_user_exist == username:
                print("-" * 30)
                print(
                    f"Welcome {username}. Please choose an option to continue.")

                while True:
                    print("-" * 60)
                    print(
                        "These codes will help you navigate: \n\n save-Create and save Credentials \n del- Delete a "
                        "saved credential \n view-Display Credentials \n find- search for saved credentials \n "
                        "copy-Copy "
                        "Password \n exit-Exit\n")
                    short_code = input("Enter option: ").lower().strip()
                    print("-" * 60)
                    if short_code == "exit":
                        print(f"Exited. Have a good day {username}!")
                        break
                    elif short_code == "save":
                        print("Save your credential. Enter details:")
                        platform_name = input("Enter the site name: ").strip()
                        username = input(
                            "Username to the site: ").strip()
                        while True:
                            print("-" * 60)
                            print(
                                "Please choose an option for entering a password: \n type-Enter your password \n "
                                "auto-Get an auto generated password \n exit-exit")
                            password_option = input(
                                "Enter an option: ").lower().strip()
                            print("-" * 60)
                            if password_option == "type":
                                password = input(
                                    "Enter your password: ").strip()
                                break
                            elif password_option == "auto":
                                password = generate_password(12)
                                break
                            elif password_option == "exit":
                                break
                            else:
                                print("Invalid Option. Try again.")
                        save_credentials(create_credentials(
                            platform_name, username, password))

                        print(
                            f"Credentials Created:\n Site Name: {platform_name} \n User Name: {username} \n "
                            f"Password: {password}")

                    elif short_code == "find":
                        print("Enter the site name you want to search for")
                        search = (input("Enter the site name: ").strip())

                        if search_credentials(search):
                            site = search_credentials(search)
                            print(
                                f"Account found: \n {site.platform_name} Account\n Username:{site.username} \n Password:{site.password}")
                        else:
                            print("Account not found")

                    elif short_code == "del":
                        print(
                            "Enter the site name of the credential you want to delete\n")
                        search = (input("Enter the site name: ").strip())
                        if search_credentials(search):
                            site = search_credentials(search)
                            delete_credentials(site)
                            print(f"Credential deleted: \n {site.platform_name} Account\n Username:{site.username} \n "
                                  f"Password:{site.password}")
                        else:
                            print("Account not found")

                    elif short_code == "view":
                        if display_credentials(username):
                            print("Here is all your saved your credentials")
                            for credential in display_credentials(username):
                                print(
                                    f"Site Name: {credential.platform_name}\t UserName: {credential.username}\t "
                                    f"Password: {credential.password}")
                        else:
                            print("You don't have any credentials saved")
                    elif short_code == "copy":
                        site_option = input(
                            "Enter the site name of which you want to copy the password: ")
                        if search_credentials(site_option):
                            site_option = search_credentials(site_option)
                            copy_credentials(site_option)
                            print(" ")
                            print(
                                f"{site_option.platform_name} account password; {site_option.password} copied to clipboard")
                    else:
                        print("Invalid. Try again.")
            else:
                print("Invalid. Try again or Create an Account.")
        else:
            print("-" * 60)
            print("Invalid. Try again.")


if __name__ == "__main__":
    password_locker()