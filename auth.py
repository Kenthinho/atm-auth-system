import sys
import random
from datetime import datetime


asterisks = '=' * 30
database = {}
my_balance = 20000

def main():
    
    print("WELCOME TO BANKPHP!")

    have_account = int(input("Do you have an account with us: 1. Yes \t 2. No \n"))

    if have_account == 1:
        login()

    elif have_account == 2:
        register()

    else:
        print("You have selected invalid option!")
        main()


def login():
    print("********** Login **********")

    user_account_number = int(input("Enter your account number here? \n"))
    password = input("Enter your password? \n")

    for account_number, user_details in database.items():
        if account_number == user_account_number and user_details[3] == password:
            now = datetime.now()
            print(f"You are welcome, {user_details[0]} {user_details[1]}!")
            print(f"You are currently logged in at {now}")
            bank_operation()
        else:
            print('Invalid account or password!!')

    
def register():
    print("********** Register **********")

    email = input("What is your email address? \n")
    first_name = input("What is your firstname? \n").upper()
    last_name = input("What is your lastname? \n").upper()
    password = input("Create a password for yourself? \n")

    account_number = account_generator()

    user_details = [ first_name, last_name, email, password ]

    database[account_number] = user_details

    print("== === ===== ===== ===")
    print("An Account Has Been Created For You!")    
    print(f"Your account number is {account_number}")
    print("Make sure you keep it safe")
    print("== === ===== ===== ===")

    login()


def bank_operation():
    selected_option = int(input("What operation would you like to carry out?\n 1. Deposit \t 2. Withdrawal \n 3. Logout \t 4. Exit \n"))

    if selected_option == 1:
        deposit_operation()

    elif selected_option == 2:
        withdrawal_operation()

    elif selected_option == 3:
        login()
    
    elif selected_option == 4:
        sys.exit()
    else:
        print("Invalid option selected!")
        bank_operation()


def withdrawal_operation(account_balance=my_balance):
    amount_withdrawn = int(input("Enter amount you want to withdraw: "))
    
    if amount_withdrawn >= account_balance:
        print("Insufficient funds!")
    else:
        account_balance -= amount_withdrawn
        print(f'Please Take Your Cash, ${amount_withdrawn}')
        print(asterisks)

    bank_operation()

def deposit_operation(account_balance=my_balance):
    amount_deposited = int(input("Enter amount to be deposited: "))
    account_balance += amount_deposited
    print(f"Your account balance is ${account_balance:,.2f}.")
    print(asterisks)

    bank_operation()


def account_generator():
    return random.randrange(1111111111, 9999999999)


if __name__ == '__main__':
    main()