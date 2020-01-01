import sqlite3
from sqlite3 import Error

class Database:
#data type to control/manage the database

    #constructor
    def __init__(self,db_file):
        self.create_connection(db_file)
        self.cursor = self.connection.cursor()

    # function that creates the connection attribute
    def create_connection(self,db_file = 'ppad6.db'):
        self.connection = None
        try:
            self.connection = sqlite3.connect(db_file)
        except Error as e:
            print(e)
        finally:
            if self.connection:
                self.connection.commit()

    #function that creates a table if it dosent exists already
    def create_table (self):
        # create a table using the statement
        sql = 'CREATE TABLE IF NOT EXSITS accounts (' \
              'username' \
              'password_hash);'
        try:
            self.cursor.execute(create_table_statment)
        except Error as e:
            print(e)

    # function that creates a row in the table that represents the accounts with usernames and passwords
    def create_account(self, username, password):
        username = scrub(username)
        password = scrub(password)
        sql = "INSERT INTO accounts (username,password_hash) VALUES (?,?);"
        self.cursor.execute(sql,(str(username),str(password)))
        self.connection.commit()
        return self.cursor.lastrowid

    # function that changes the password to a specified account
    def update_account(self, username, password_hash):
        username = scrub(username)
        password = scrub(password)
        sql = ''' UPDATE accounts SET username = ? password_hash = ?'''
        self.cursor.execute(sql, (username,password_hash))
        self.connection.commmit()

    # function that selects all the rows in the accounts table
    def select_all_accounts(self):
        self.cursor.execute("SELECT * FROM accounts;")
        rows = self.cursor.fetchall()
        return rows

    # functiont that selects a specified account
    def select_account(self,given_username):
        given_username = scrub(given_username)
        self.cursor.execute("SELECT * FROM accounts WHERE username = ?;",(given_username,))
        rows = self.cursor.fetchall()
        return rows

    # function that deletes an row from the table with a specified username
    def delete_account(self,username):
        username = scrub(username)
        sql = 'DELETE FROM accounts WHERE username = ?;'
        self.cursor.execute(sql,username)
        self.connection.commit()
    # function that deletes all rows from the table
    def delete_all_accounts(self):
        sql = 'DELETE FROM accounts;'
        self.cursor.execute(sql)
        self.connection.commit()

    @staticmethod
    def scrub(string):
        return ''.join(char for char in string if car.isalnum())