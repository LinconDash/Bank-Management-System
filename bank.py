# Bank Services
from database import *
from datetime import datetime

class Bank:
    def __init__(self, username, account_number):
        self.__username = username
        self.__account_number = account_number
        self.create_transactiontable()
    
    def create_transactiontable(self):
        query(f'''CREATE TABLE IF NOT EXISTS {self.__username}_transactions (
                timedate varchar(40),
                account_number int,
                remarks varchar(30),
                amount float)
            ''')
        return
    
    def deposit(self, amount):
        temp = query(f"SELECT balance FROM customers WHERE username = '{self.__username}' AND account_no = '{self.__account_number}';")
        temp2 = query(f"UPDATE customers SET balance = {temp[0][0] + amount} WHERE username = '{self.__username}' AND account_no = '{self.__account_number}';") 
        print(f"AMOUNT of Rs.{amount} deposited successfully to account number {self.__account_number}")
        self.balance_enquiry()
        query(f"INSERT INTO {self.__username}_transactions VALUES ('{datetime.now()}', '{self.__account_number}', 'Amount Deposit', {amount});")
        db.commit()
        return
    
    def balance_enquiry(self):
        temp =  query(f"SELECT balance FROM customers WHERE username = '{self.__username}' AND account_no = '{self.__account_number}';")
        print(f"Available Balance Rs: {temp[0][0]}")
        return

    def withdraw(self, amount):
        temp = query(f"SELECT balance FROM customers WHERE username = '{self.__username}' AND account_no = '{self.__account_number}';")
        if temp[0][0] >= amount:
            temp2 = query(f"UPDATE customers SET balance = {temp[0][0] - amount} WHERE username = '{self.__username}' AND account_no = '{self.__account_number}';") 
            print(f"AMOUNT of Rs.{amount} withdraw successfully from account number {self.__account_number}")
            self.balance_enquiry()
            query(f"INSERT INTO {self.__username}_transactions VALUES ('{datetime.now()}', '{self.__account_number}', 'Amount Withdraw', {amount});")
            db.commit()
            return
        else:
            print("Amount Exceeds Available Balance !!!")
            return
    
    def fund_transfer(self, amount):
        temp = query(f"SELECT balance FROM customers WHERE username = '{self.__username}' AND account_no = '{self.__account_number}';")
        if temp[0][0] >= amount:
            acc2 = input("Enter the other account number: ")
            valid = query(f"SELECT COUNT(1) FROM customers WHERE account_no = '{acc2}';")
            if valid[0][0] != 0:
                try:       
                    reciever_name = query(f"SELECT username FROM customers WHERE account_no = '{acc2}';")
                    query(f"UPDATE customers SET balance = balance - {amount} WHERE username = '{self.__username}' AND account_no = '{self.__account_number}';")                                       
                    query(f"UPDATE customers SET balance = balance + {amount} WHERE account_no = '{acc2}';")                                        
                    query(f"INSERT INTO {self.__username}_transactions VALUES ('{datetime.now()}', '{self.__account_number}', 'Fund transfer to {acc2}', {amount});")
                    query(f"INSERT INTO {reciever_name[0][0]}_transactions VALUES ('{datetime.now()}', '{acc2}', 'Fund Recieve from {self.__account_number}', {amount});")
                    db.commit()                  
                    print(f"AMOUNT of Rs.{amount} transferred from Account: {self.__account_number} to Account: {acc2}")
                except Exception as e:
                    db.rollback()
                    print(f"An error occurred: {e}")
            else:
                print("Please select a valid account number!")
        else:
            print("Insufficient balance!")

