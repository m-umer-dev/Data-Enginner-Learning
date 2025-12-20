#Program 01

class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance   # private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successful")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance")
        elif amount <= 0:
            print("Withdraw amount must be positive")
        else:
            self.__balance -= amount
            print("Withdrawal successful")

    def get_balance(self):
        return self.__balance


acc = BankAccount()

acc.deposit(500)
acc.withdraw(200)
print("Current Balance:", acc.get_balance())