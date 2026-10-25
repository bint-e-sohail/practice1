# Custom Exception
class InsufficientFundsError(Exception):
    pass

# Bank Account Class
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(f"Cannot withdraw {amount}, balance is {self.balance}")
        self.balance -= amount

# Main task

# Start with 1000, deposit 500, withdraw 300
acc = BankAccount("User", 1000)
acc.deposit(500)
acc.withdraw(300)

# Print balance
print(acc.balance)

# Try to withdraw 5000 and catch the error
try:
    acc.withdraw(5000)
except InsufficientFundsError as e:
    print(f"Error: {e}")