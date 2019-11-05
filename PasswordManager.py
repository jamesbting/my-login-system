from Account import Account
from pip._vendor.distlib.compat import raw_input

def findAccount(username, accountList):
    for i in range(0,len(accountList)):
        temp = accountList[i]
        if Account.getUsername(temp) == username :
            return i
    return -1

def checkPassword(account,string):
    if account.password != string:
        return False
    return True

def loginFunction(username,accountList):
    i = findAccount(username,accountList)
    if i != -1:
        temp = accountList[i]
        input = raw_input("Enter the password for " + str(Account.getUsername(temp) + ": "))
        isCorrect = checkPassword(temp, input)
        if (isCorrect == True):
            print("Login Successful. Access Granted")
        else:
            print("Username or Password is incorrect")
    return

def createAccountFunction(accountList) -> object:
    input = raw_input("New Username: ")
    newUsername = input
    i = findAccount(newUsername,accountList)
    if i == -1:
        input = raw_input("Password: ")
        newPassword  = input
        input = raw_input("Confirm Password: ")
        confirmPassword = input
        if(confirmPassword == newPassword):
            newAccount = Account(newUsername, newPassword)
            accountList.append(newAccount)
            print("Account created succesfully!")
            return
        else:
            print("The passwords must match!")
            return
    else:
        print("That username is already taken. Please try again")
        return

def changePasswordFunction(username,accountList):
    i = findAccount(username,accountList)
    if i != -1:
        account = accountList[i]
        input = raw_input("Enter the old password: ")
        oldPassword = input
        if oldPassword != Account.getPassword(account):
            print("Verify the old password is correct")
            return
        input = raw_input("Enter the new password: ")
        newPassword = input
        input = raw_input("Confirm the new password: ")
        confirmPassword = input
        if newPassword != confirmPassword:
            print("The passwords must match!")
        Account.changePassword(account,newPassword)
        print("Password changed sucessfully!")

def main():
    file = open("Account List.txt","r")
    accounts = file.readlines()
    file.close()
    accountList = []
    for i in range(len(accounts)):
        tempUsername, tempPassword = accounts[i].split()
        newAccount = Account(tempUsername,tempPassword)
        accountList.append(newAccount)

    print("a) Login")
    print("b) Create an Account")
    print("c) Change Password")
    print("d) Terminate Program")
    input = raw_input("What would you like to do? Enter the letter of your desired action: ")
    while(input != None):
        if input == "a" or input == "A":
            input = raw_input("Enter your username: ")
            loginFunction(input,accountList)
        elif input == "b" or input == "B":
            createAccountFunction(accountList)
        elif input == "c" or input == "C":
            input = raw_input("Which accounts' password would you like to change?")
            changePasswordFunction(input,accountList)
        elif input == "d" or input == "D":
            file = open("Account List.txt","w")
            for i in range(len(accountList)):
                temp = accountList[i]
                username = Account.getUsername(temp)
                password = Account.getPassword(temp)
                file.write (username + " " + password + "\n")
            print("Terminating Program. Goodbye")
            break;
        else:
            print("Your input is invalid. Please try again!")
        print()
        print("a) Login")
        print("b) Create an Account")
        print("c) Change Password")
        print("d) Terminate Program")
        input = raw_input("What would you like to do? Enter the letter of your desired action: ")

main()





