# Bank Database Management
import mysql.connector as sql
import os

os.environ["db-password"] = "your-mysql-password"


db = sql.connect(
    host="localhost",
    user="root",
    passwd=os.environ.get("db-password"),
    database="bank"
)

cursor = db.cursor()

def createcustomertable():
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
        username varchar(30) not null,
        password varchar(20) not null,
        name varchar(20) not null,
        age int,
        city varchar(20) not null,
        account_no int unique not null,
        balance float not null,
        status boolean not null)    
        ''')

def query(string):
    cursor.execute(string)
    result = cursor.fetchall()
    return result

db.commit()

if __name__ == "__main__":
    createcustomertable()
