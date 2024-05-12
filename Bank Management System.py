class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            print("Deposit amount cannot be negative.")
            return
        self.balance += amount
        print(f"Deposited Rs.{amount:.2f}")
        print(f"New balance: Rs.{self.balance:.2f}")

    def withdraw(self, amount):
        if amount < 0:
            print("withdrawal amount cannot be negative.")
            return
        elif amount > self.balance:
            print("Insufficient funds.")
            return
        self.balance -= amount
        print(f"Deposited Rs.{amount:.2f}")
        print(f"New balance: Rs.{self.balance:.2f}")

    def transfer(self, other_account, amount):
        if amount < 0:
            print("Transfer amount cannot be negative.")
            return
        elif amount > self.balance:
            print("Insufficient funds.")
            return
        self.balance -= amount
        print(f"Transferred Rs.{amount:.2f} to account {other_account.account_number}")
        print(f"remaining balance is Rs.{self.balance:.2f}")


accounts = {} #this is the dictionary that will store account numbers as keys and corresponding 

def create_account():
    account_number = len(accounts) + 23010791 #generates a unique bank account number

    while account_number in accounts:
        account_number += 1

    initial_deposit = float(input("Enter initial deposit amount: Rs."))
    if initial_deposit < 0:
        print("Initial deposit cannot be negative.")
        return

    accounts[account_number] = Account(account_number, initial_deposit)
    print(f"Account create successfully. Account number: {account_number}")


def deposit():
    account_number = int(input("Enter your account number: "))
    if account_number not in accounts:
        print("Account does not exist.")
        return
    amount = float(input("Enter your deposit amount: Rs."))
    accounts[account_number].deposit(amount)

def withdraw():
    account_number = int(input("Enter your account number: "))
    if account_number not in accounts:
        print("Account does not exist.")
        return
    amount = float(input("Enter your withdraw amount: Rs."))
    accounts[account_number].withdraw(amount)

def balance_check():
    account_number = int(input("Enter your account number: "))
    if account_number not in accounts:
        print("Account does not exist.")
        return
    print(f"Balance: Rs.{accounts[account_number].balance:.2f}")


def transfer():
    sender_account_number = int(input("Enter your account number: "))
    if sender_account_number not in accounts:
        print("Account does not exist.")
        return
    recipient_account_number = int(input("Enter recipient account number: "))
    if recipient_account_number not in accounts:
        print("Account does not exist.")
        return
    amount = float(input("Enter your withdraw amount: Rs."))
    accounts[sender_account_number].transfer(accounts[recipient_account_number], amount)


def main(): #display the menu and get the user's choice.
    print("\nWelcome to Bank Account Management System.")
    print("choice 1. Create a new account")
    print("choice 2. Deposit money")
    print("choice 3. Withdraw money")
    print("choice 4. Check my account balance")
    print("choice 5. Transfer money")
    print("choice 6. Exit")
    choice = input("Enter your choice: ")
    return choice


while True:
    choice = main()
    if choice == '1':
        create_account()
    elif choice == '2':
        deposit()
    elif choice == '3':
        withdraw()
    elif choice == '4':
        balance_check()
    elif choice == '5':
        transfer()
    elif choice == '6':
        print("Exit")
        break
    else:
        print("invalid choice. ")
