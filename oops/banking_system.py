class BankAccount:
    def __init__(self):
        self.balance = 0 # Open a new Bank Account
        print("Welcome to the ABC Bank!")

    def deposit(self):
        amount = float(input("Enter amount to be Deposited: "))
        self.balance = amount
        print("\n Amount Deposited ", amount)

    def withdraw(self):
        amount = float(input("Enter amount to be withdraw: "))
        if(self.balance < amount):
            print(" Insuffucient Balance ") 
        self.balance -= amount
        print("\n Amount Withdrawn ", amount)

    def checkBalance(self):
        print("Your Current Balance is : ",self.balance)

account = BankAccount()

account.checkBalance()
account.deposit()
account.checkBalance()
