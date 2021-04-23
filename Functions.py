import random
import datetime
import validation
import database

details = {}


def init():
    print("Welcome to Bank Marliz")
    import datetime
    x = datetime.datetime.now()
    print(x)
    haveAccount = int(input("Do you have an account with us? \nPress 1 to Register: \nPress 2 to Login: \n"))
    if haveAccount == 1:
        register()
    elif haveAccount == 2:
        login()
    else:
        print("Invalid Option")
        init()

    return None


def register():

    print("Register Here...")
    firstName = input("Enter first name \n")
    lastName = input("Enter last name \n")
    email = input("Enter your email address \n")
    accountPin = int(input("Enter a 4 digit pin\n"))
    accountNumber = generateAccountNumber()
    balance = 0

    # details[accountNumber] = ([firstName, lastName, email, accountPin, balance])

    is_user_created = database.create(accountNumber, [firstName, lastName, email, accountPin, balance])

    if is_user_created:
        print("Your Account Number is" ,accountNumber)
        print("Account created.\nLogin to access account")
        login()
    else:
        print("An error occurred\nPlease try again")
        register()

    # return None


def login():
    import datetime
    x = datetime.datetime.now()
    print(x)
    print("Log in here...")

    accountNumberInputted = input("Enter your Account Number \n")

    isValidAccountNumber = validation.accountNumberValidation(accountNumberInputted)

    if isValidAccountNumber:
        accountPin = int(input("Enter your pin...\n"))
        for accountNumber, userDetails in details.items():
            if accountNumber == int(accountNumberInputted) and userDetails[3] == (accountPin):
                print("yes")
                bankOperations(userDetails, accountNumber)
            else:
                print("Login unsuccessful.\n Invalid account number or pin")
                login()


def bankOperations(userDetails, accountNumber):
    first_name = userDetails[0]
    last_name = userDetails[1]
    print(f"Welcome {first_name.upper()} {last_name.upper()} ")
    print("What would you like to do?...\n1 = Deposit\n2 = Withdrawal\n3 = Balance\n4 = Change Pin\n5 = Log out\n6 = Exit")

    bankOperations_options = int(input("Select an option...\n"))
    if bankOperations_options == 1:
        deposit(accountNumber, userDetails)
    elif bankOperations_options == 2:
        withdraw(accountNumber, userDetails)
    elif bankOperations_options == 3:
        checkBalance(accountNumber, userDetails)
    elif bankOperations_options == 4:
        changePin(accountNumber, userDetails)
    elif bankOperations_options == 5:
        logout()
    elif bankOperations_options == 6:
        exit()
    else:
        print("Invalid Option")
        bankOperations(userDetails, accountNumber)


def generateAccountNumber():
    import random
    return random.randint(1111111111, 9999999999)
    print("Your Account Number is " + str(accountNumber))

def deposit(accountNumber, userDetails):
    depositAccountNumber = int(input("Enter the account number you want to deposit into...\n"))
    if depositAccountNumber == accountNumber:
        print("Enter deposit amount...")
        depositAmount = int(input("How much do you wish to deposit?...\n"))
        balance = userDetails[4]
        currentBalance = balance + depositAmount
        print("Your current balance is " +str(currentBalance))
        print("Do you want to perform another operation?...")
        print("What would you like to do?...\n1 = Deposit\n2 = Withdrawal\n3 = Balance\n4 = Change Pin\n5 = Log out\n6 = Exit")

def withdraw(accountNumber, userDetails):
    withdrawalAccountNumber = int(input("Enter account number\n"))
    if withdrawalAccountNumber == accountNumber:
        withdrawalAmount = int(input("How much would you like to withdraw?.../=\n"))
        balance = userDetails[4]
        if withdrawalAmount > balance:
            print("Insufficient Funds")
        else:
            print(str(withdrawalAmount) + " has been withdrawn")
            print("Your current balance is " + str((balance - withdrawalAmount)))
            print("What would you like to do?...\n1 = Deposit\n2 = Withdrawal\n3 = Balance\n4 = Change Pin\n5 = Log out\6 = Exit")
    else:
        print("Account does not exist")

def checkBalance(accountNumber, userDetails):
    balanceAccountNumber = int(input("Enter account number\n"))
    if balanceAccountNumber == accountNumber:
        balance = userDetails[4]
        print(balance)
        print("What would you like to do?...\n1 = Deposit\n2 = Withdrawal\n3 = Balance\n4= Change Pin\n5 = Log out\6 = Exit")
    else:
        print("Invalid Account Number")

def changePin(accountNumber, userDetails):
    account_number = int(input("Enter account number\n"))
    if account_number == accountNumber:
        accountPinEntry = int(input("Enter your Pin\n"))
        if accountPinEntry == userDetails[3]:
            newPin = int(input("Enter 4 digits\n"))
            isValidAccountPin = validation.accountPinValidation(newPin)
            if isValidAccountPin:
                accountPin = userDetails[3]
                accountPin = newPin
                print("Your pin is " + str(newPin))
        else:
            print("Invalid pin")
    else:
        print("Invalid Account Number")

def exit():
    print("Exiting...")
    quit()

def logout():
    print("Logging out...")
    import sys
    sys.exit(login())


init()