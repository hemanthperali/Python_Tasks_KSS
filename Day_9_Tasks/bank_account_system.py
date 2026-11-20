'''A bank wants to manage customer accounts. Create a BankAccount class with a
constructor to initialize account number and balance. Implement methods to deposit,
withdraw, and display balance.'''

class BankAccount:
    def __init__(self,account_number,balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self,amount):
        if amount > 0:
            self.balance+=amount

    def withdraw(self,amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient Balance")

    def display(self):
        return self.balance

b = BankAccount(18910100,6000)
b.deposit(4000)
b.withdraw(2000)

print("Remaining balance:", b.display())
