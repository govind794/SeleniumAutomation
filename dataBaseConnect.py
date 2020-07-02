'''
DDl (Data Definition Language) -- create, alter, drop, rename, truncate, comment
DML (Data Manipulation Language) -- insert, update, delete, merge, call
DRL (Data Retrieval Language) -- select
DCL (Data Control Language) -- grant, revoke
TCL (Transaction Control Language) -- commit, savepoint, rollback
'''

import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='justride',
                                         user='root',
                                         password='govind')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select email from sys_users where id = 92251;")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
