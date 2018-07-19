class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.show_balance()

    def withdraw(self, amount):
        if 0 < amount < self.balance:
            self.balance -= amount
        else:
            print("insufficient balance")
        self.show_balance()

    def show_balance(self):
        print("Balance is {}".format(self.balance))


