class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance


account = BankAccount(100)

print("Initial balance:", account.get_balance())

account.deposit(50)        
print("Balance after deposit:", account.get_balance())

account.withdraw(120)    
print("Balance after withdrawal:", account.get_balance())

account.withdraw(50)     
print("Final balance:", account.get_balance())