import os,sys

names = open('names.txt','a')
passwords = open('passwords.txt','a')

check_names = names.read()
check_passwords = passwords.read()


def ChckLoginInfo():
    check_1 = input("Enter username")
    
    if check_1 in check_names:
        print("Welcome back, ",check_1)
        return check_1,0
    else:
        return "new user",1

def NewLoginInfo():
    if ChckLoginInfo()[1] == 1:
        Name = str(input("Please enter your name:\t"))        
        names.write(Name)
        Password = str(input("Enter your password:\t"))
        passwords.write(Password)


names.close()
passwords.close()


