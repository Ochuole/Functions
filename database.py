# noinspection PyTrailingSemicolon
import os
import validation

user_db_path = "data/user_record/"


def create(accountNumber, userDetails):
    global f
    completion_state = False

    try:
        f = open("data/" + str(accountNumber) + ".txt", "x")
    except FileExistsError:
        print("User already exists")

    else:
        f.write(str(userDetails))
        completion_state = True
    finally:
        f.close()
        return completion_state


def update(userDetails):
    print("Update record")


#     search for user using account number
# fetch file content
# update file content
# save the file

def read(accountNumber):
    global f
    is_valid_account_number = validation.accountNumberValidation(accountNumber)
    try:
        if is_valid_account_number:
            f = open(user_db_path + str(accountNumber) + ".txt", "r")

        else:
            f = open(user_db_path + accountNumber + ".txt", "r")

    except FileNotFoundError:
        print("File not found")
    except FileExistsError:
        print("File does not exist")
    else:
        f.readline()


def delete(accountNumber):
    is_delete_successful = False
    try:
        os.remove(user_db_path + str(accountNumber) + ".txt" "x")
        is_delete_successful = True
    except FileNotFoundError:
        print(user_db_path + str(accountNumber) + ".txt")
        print("User not found\nCheck account number and try again")
    finally:
        return is_delete_successful


# search for user using account number
# fetch file content
# delete user record
# return True

def does_email_address_exist(email):
    all_users = os.listdir(user_db_path)
    for user in all_users:
        user_list = str.split(read(user), ",")
        if email in user_list:
            return True
    return False
def does_account_number_exist(accountNumber):
    all_users = os.listdir(user_db_path)
    for user in all_users:
        if user == str(accountNumber) + ".txt":
            return True
    return False


