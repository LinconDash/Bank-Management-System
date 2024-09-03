from register import *
from database import *

print("BANK OF INDIA")
print("WELCOMES YOU !!!")

status = False

while True:
    try:
        register = int(input("1. SignUp\n"
                             "2. SignIn\n"
                             "3. EXIT\n"))

        if register in [1,2,3]:
            if register == 1:
                SignUp()
                break
            elif register == 2:
                user = SignIn()
                status = True
                break
            else:
                break
        else:
            print("Please Enter Valid Input from Options given above.")
    except ValueError:
        print("Invalid Input , Try Again (only digits allowed)!")

if status:
    temp = query(f"SELECT account_no FROM customers WHERE username = '{user}'")
    account = temp[0][0]
    
while status:
    print(f"WELCOME {user.upper()} , PLEASE SELECT YOUR BANKING SERVICES")
    try:
        facility = int(input("1. Balance Enquiry\n"
                             "2. Cash deposit\n"
                             "3. Cash withdraw\n"
                             "4. Fund Transfer\n"
                             "Press Anyother key to EXIT.\n"))

        if facility in [1,2, 3, 4]:
            b = Bank(user, account)
            if facility == 1:
                b.balance_enquiry()
            elif facility == 2:
                amount = float(input("Deposit Amount Rs: "))
                b.deposit(amount)
            elif facility == 3:
                amount = float(input("Withdraw Amount Rs. "))
                b.withdraw(amount)
            elif facility == 4:
                amount = float(input("Amount to be transferred Rs. "))
                b.fund_transfer(amount)
        else:
            break
    except ValueError:
        print("Invalid Input , Try Again (only digits allowed) !")
        continue

print("THANK YOU !")