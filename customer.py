# Customer Details
from database import *

class Customer:
    def __init__(self, username, password, name, age, city, account_number, balance):
        self.__username = username
        self.__password = password
        self.__name = name
        self.__age = age
        self.__city = city
        self.__account_number = account_number
        self.__balance = balance

    def create_user(self):
        temp = query(f"INSERT INTO customers VALUES ('{self.__username}', '{self.__password}', '{self.__name}', '{self.__age}', '{self.__city}', '{self.__account_number}','{self.__balance}', True)")
        db.commit()
        print("User created successfully !")