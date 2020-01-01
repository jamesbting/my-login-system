import math
from pip._vendor.distlib.compat import raw_input
import hashlib as hash
import yaml
from Database import Database

class LoginSystem:
    # constructor
    def __init__(self,file_name):
        file = open(file_name,'r')
        self.database_info = yaml.safe_load(file) # load the name of the database file from the config file
        self.database = Database(self.database_info[0])

    # function to find a specified account in the dictionary
    def __find_account(self,username):
        account = self.database.select_account(username)
        return account

    @staticmethod
    # function that takes as input a string and returns the SHA 256 hash in hexidecimal
    def __convert_to_hash(string):
        h = hash.sha256()
        h.update(string.encode('utf-8'))
        return h.hexdigest()

    # function to check if a given password is valid
    def __check_password(self,username, given_password):
        account = self.__find_account(username)
        hashed_given = self.__convert_to_hash(given_password)
        return account[0][1] == hashed_given


    # function to login the user, as long as the given password is correct for the username
    def login_function(self,username, password):
            return self.__check_password(username, password)

    # function to create an account, as long as the username provided is unique
    def create_account(self, new_username, new_password):
        account = self.__find_account(new_username)
        if len(account) == 0:
            self.database.create_account(new_username, self.__convert_to_hash(new_password))
            return True
        return False

    # function to change the password of a specified account, if it exists
    def change_password(self, username, old_password, new_password):
        try:
            if self.__find_account(username) != None and self.__check_password(username,old_password):
                self.database.update_account(username,__convert_to_hash(new_password))
                return True
        except Error as e:
            return False




