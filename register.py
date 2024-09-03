# User registration SignIn / SignUp
from database import *
from customer import *
from bank import *
import random

def SignUp():
    username = input("Create Username : ")
    temp = query(f"SELECT username FROM customers WHERE username='{username}'")
    if temp:
        print("Username Already Exists, Please Try Again !")
        SignUp()
    else:
        print("Username is Available, Please Proceed !")
        password = input("Enter your Password : ")
        name = input("Enter your name : ")
        age = int(input("Enter your Age : "))
        city = input("Enter your city : ")
        while True:
            account_no = random.randint(10000000, 99999999)
            temp = query(f"SELECT account_no FROM customers WHERE account_no='{account_no}'")
            if temp:
                continue
            else:
                print("Account Number : ", account_no)
                break
        
    c = Customer(username, password, name, age, city, account_no, 0) 
    c.create_user()  
    b = Bank(username, account_no) 
    b.create_transactiontable()
    print("Your transactions are online now !")
    return

def SignIn():
    username = input("Enter Username : ")
    temp = query(f"SELECT username FROM customers WHERE username = '{username}'")
    if temp:
        while True:
            password = input("Enter your Password : ")
            temp = query(f"SELECT password FROM customers WHERE username='{username}'")
            if temp[0][0] == password:
                print("Signed In Successfully")
                return username
            else:
                print("Wrong Password, Please Try Again !")
                continue
    else:
        print("Incorrect Username, Try Again !")
        SignIn()
