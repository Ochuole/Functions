def accountNumberValidation(accountNumber):
    if accountNumber:
        if len(str(accountNumber)) == 10:
            try:
                int(accountNumber)
                return True
            except ValueError:
                print("Account Number should be Numbers")
                return False
            except TypeError:
                print("Invalid Account Number")
                return False
        else:
            print("Account Number cannot be less than 10 digits")
            return False

    else:
        print("account number required")
        return False

def registrationValidation(userDetails):
    if userDetails:
        if userDetails == type(list):
            try:
                len(userDetails) == 4
                return True
            except TypeError:
                print("User details incomplete")
    else:
        print("Incomplete user details")


def accountPinValidation(newPin):
    if newPin:
        if len(str(newPin)) == 4:
            try:
                int(newPin)
                return True
            except ValueError:
                print("Account Pin should be Numbers")
                return False
            except TypeError:
                print("Invalid Account Pin")
                return False
        else:
            print("Account pin cannot be less than 4 digits")
            return False

    else:
        print("Account pin required")
        return False
    # check if it is list
    # check item to see if the data type is valid
    # check to see if the pin inputted is 4 digits
    # check to see if the pin inputted is an integer