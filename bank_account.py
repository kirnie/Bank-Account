#!/usr/bin/python3

class BankAccount():
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    #introduce bank account
    def __repr__(self):
        return "{}'s account".format(self.name)

    #show current balance on bank account
    def show_balance(self):
        print("""{}:
Balance: €{:.2f}""".format(self, self.balance))

    #deposit money to bank account
    def deposit(self, amount):
        if amount <= 0:
            return "You have entered invalid value."
        else:
            self.balance += amount
            print("""{}:
You have deposited €{:.2f}""".format(self, amount))

    #withdraw money
    def withdraw(self, amount):
        if amount > self.balance:
            print("""{}:
You have not enough money.""".format(self))
        else:
            print("""{}:
Withdraw: €{:.2f}""".format(self, amount))
            self.balance -= amount
            self.show_balance()

    #make payment
    def make_payment(self, amount, account):
        self.account = account
        if amount > self.balance:
            print("""{}:
You have not enough money for that payment.""".format(self))
        else:
            self.balance -= amount
            account.balance += amount
            print("""{}:
{:.2f} sent to {}""".format(self, amount, account))


Ernie = BankAccount("Ernie", 0)
Veronika = BankAccount("Veronika", 0)

Veronika.show_balance()
Veronika.deposit(1000)
Veronika.make_payment(555, Ernie)
Ernie.show_balance()
Ernie.withdraw(800)
Ernie.withdraw(250)
