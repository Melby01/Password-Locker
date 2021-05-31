#!/usr/bin/env python3.8
from user import User
from password import Password

def create_user(user_name,password):
    '''
    Function to create a new user
    '''
    new_user = User(user_name,password)
    return new_user

def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()
    
def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()
    
def find_user(user_name):
    '''
    Function that finds a user by number and returns the user
    '''
    return User.find_by_user_name(user_name)

def check_existing_users(user_name):
    '''
    Function that check if a user exists with that number and return a Boolean
    '''
    return User.user_exist(user_name)

def display_users():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()



def create_password (user_name1,password,handle):
    '''
    Function to create a new password credentials
    '''
    new_password = Password()
    return new_password

def save_password(password):
    '''
    Function to save password credentials
    '''
    password.save_password()
    
def delete_password(password):
    '''
    Function to delete a password credentials
    '''
    password.delete_password()
    
def find_password_by_number(number):
    '''
    Function that finds a credentials by user_name and returns the credentials
    '''
    return Password.find_by_number(number)

def existing_password(password):
    '''
    Function that check if a credentials exists with that number and return a Boolean
    '''
    return Password.password_exist(password)

def display_password():
    '''
    Function that returns all the saved credentials
    '''
    return Password.display_password()



def main():
    print("Hi there! PLease Insert Your username!")
    print("Welcome to Password Locker. Insert these to proceed:CH = create handle,")
    short_code = input().lower()
    
    if short_code == 'ch':
        print('Insert new handle details')
        print('*' * 100)
        handle = input('Enter handleName: ')
        username = input('Enter Username: ')
       
        while True:
            print('use : EP = enter password')
            password_choice = input().lower()
            if password_choice == 'ep':
                password = input('Enter Password: ')
                break
            else:
                print('Invalid short_code. Please try again')
                save_user(create_user(username, password))
            
            print('*' * 100)
            print('Welcome {username} to your new handle, your password is <--- {password} --->')
            print('*' * 100)
            
            while True:
                print('Use these short codes to manage passwords: \n NC = new credential, \n VC = display credentials,\n SC =  find credential  \n Dc = delete credential, \n  EX = exit application')
                short_code = input().lower()
                if short_code == 'nc':
             print('Enter New Credential Details')
             print('*' * 100)
             handle = input('Handle Name : ')
             user_name1 = input('Username : ')
             while True:
                print('Use: EP = enter password?')
                password_choice = input().lower()
                if password_choice == 'ep':
                    password = input('Enter password : ')
                    break
                else:
                    print('Invalid short code. Please try again')
                print('*' * 100)
            save_password(create_password(handle, user_name1,password))
            print('*' * 100)
            print(f'Your {handle} handle has been saved')
            print('*' * 100)
    elif short_code == 'vc':
            if display_password():
                print('Your saved credentials are:')
                for handle in display_password():
                    print('*' * 100)
                    print(f' Name: {handle} \n Username: {user_name1} \n Password: {password}')
                    print('*' * 100)
            else:
                print('*' * 100)
                print('You have No Credentials. Please Create One')
                print('*' * 100)
    elif short_code == 'dc':
            print('Enter Handle name to delete...')
            name = input('Handle Name : ')
            print('*' * 100)
            if find_password_by_number(number):
                name_result = find_password_by_number(number)
                name_result.delete_password()
                print(f'Handle {name} has been successfully deleted ')
                print('*' * 100)
            else:
                print('Incorrect handle name')
                print('*' * 100)
    elif short_code == 'sc':
            print('Enter Handle Name To Search...')
            search = input('Handle Name : ')
            print('*' * 100)
            if find_password_by_number(search):
                search = find_password_by_number(search)
                print(f'Handle Name: {search} ')
                print('*' * 100)
            else:
                print('Credentials does not exist')
                print('*' * 100)
    elif short_code == 'ex':
            print('Goodbye')
            print('*' * 100)
        break
    else:
            print('Invalid Short code. Please try again!')
            print('*' * 100)
if __name__ == '__main__':
    main()

def main():
    print("Hello! PLease insert your username!")
    print('Welcome to the Password-locker. Apply these commands to continue: CH = create handle,' )
    short_code = input().lower()
    if short_code == 'ch':
        print('Enter new handle details')
        print('*' * 100)
        username = input('Enter Username: ')
        while True:
            print('use :  EP = to manually enter your own password')
            password_choice = input().lower()
            if password_choice == 'ep':
                password = input('Enter Password: ')
                break
            else:
                print('Invalid short code. Please try again')
            save_user(create_user(user_name, password))
        print('*' * 100)
        print(f'Welcome {username} to your new handle your password is <--- {password} --->')
        print('*' * 100)
    while True:
        print('Use these short codes to manage credentials: \n NC = new credential, \n VC = display credentials,\n SC =     find credential  \n Dc = delete credential, \n  EX = exit application')
        short_code = input().lower()
        if short_code == 'nc':
            print('Enter New Credentials Details')
            print('*' * 100)
            handle = input('Handle Name : ')
            user_name1 = input('Username : ')
            while True:
                print('Use: EP = manually enter password?')
                password_choice = input().lower()
                if password_choice == 'ep':
                    password = input('Enter password : ')
                    break
                else:
                    print('Invalid short code. Please try again')
                print('*' * 100)
            save_password(password) 
            print('*' * 100)
            print(f'Your {handle} handle has been saved')
            print('*' * 100)
        elif short_code == 'vc':
            if display_password():
                print('Your saved credentials are:')
                for handle in display_password():
                    print('*' * 100)
                    print(f' Name: {handle} \n Username: {user_name1} \n Password: {password}')
                    print('*' * 100)
            else:
                print('*' * 100)
                print('You have No Credentials. Please Create One')
                print('*' * 100)
        elif short_code == 'dc':
            print('Enter Handle name to delete...')
            name = input('Handle Name : ')
            print('*' * 100)
            if find_password_by_number(number):
                name_result = find_password_by_number(number) 
                name_result.delete_password()
                print(f'Handle {name} has been successfully deleted ')
                print('*' * 100)
            else:
                print('Incorrect handle name')
                print('*' * 100)
        elif short_code == 'sc':
            print('Enter Handle Name To Search...')
            search = input('Handle Name : ')
            print('*' * 100)
            if find_password_by_number(search):
                search = find_password_by_number(search)
                print(f'Handle Name: {search} ')
                print('*' * 100)
            else:
                print('Credentials does not exist')
                print('*' * 100)
        elif short_code == 'ex':
            print('Goodbye')
            print('*' * 100)
            break
        else:
            print('Invalid Short code. Please try again!')
            print('*' * 100)
            
if __name__ == '__main__':
    main()

            
            