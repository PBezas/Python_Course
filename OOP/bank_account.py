# Bank Account OOP Exercise
# Define a new class called BankAccount.

# Each BankAccount should have an owner , specified when a new BankAccount is created like BankAccount("Charlie")
# Each BankAccount should have a balance attribute  that always starts out as 0.0
# Each instance should have a deposit method that accepts a number and adds it to the balance. It should return the new balance.
# Each instance should have a withdraw method that accepts a number and subtracts it from the balance. It should return the new balance.
# acct = BankAccount("Darcy")
# acct.owner #Darcy
# acct.balance #0.0
# acct.deposit(10)  #10.0
# acct.withdraw(3)  #7.0
# acct.balance .  #7.0


class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def get_balance(self):
        return self.balance

    def deposit(self, ammount):
        self.balance += ammount
        return self.balance

    def withdraw(self, ammount):
        self.balance -= ammount
        return self.balance


account1 = BankAccount("Panos Bezas")

print(f"The owner of this account is {account1.owner}")
print(f"The total ammount of money inside this account is {account1.get_balance()} €")

deposit_ammount = 150
account1.deposit(deposit_ammount)
print(f"You deposited {deposit_ammount} €")
print(f"The new balance of the account is {account1.get_balance()} €")

withdraw_ammount = 50
account1.withdraw(50)
print(f"You withdrew {withdraw_ammount} €")
print(f"The new balance of the account is {account1.get_balance()} €")
