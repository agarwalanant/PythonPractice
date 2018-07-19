


class Account:
    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance
        self.show_balance()

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Aomunt deposited")
            self.show_balance()

    def withdraw(self, amount):
        if 0 < amount < self.__balance:
            self.__balance -= amount
            print("Amount Withdrawn")
        else:
            print("insufficient balance")
        self.show_balance()

    def show_balance(self):
        print("Balance is {}".format(self.__balance))


Anant = Account("Anant", 1000)

Anant.deposit(1000)
Anant.withdraw(200)
Anant.withdraw(5000)

