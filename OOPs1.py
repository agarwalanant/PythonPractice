class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Aomunt deposited")
            self.show_balance()

    def withdraw(self, amount):
        if 0 < amount < self.balance:
            self.balance -= amount
            print("Amount Withdrawn")
        else:
            print("insufficient balance")
        self.show_balance()

    def show_balance(self):
        print("Balance is {}".format(self.balance))


Anant = Account("Anant", 1000)

Anant.deposit(1000)
Anant.withdraw(200)
Anant.withdraw(5000)