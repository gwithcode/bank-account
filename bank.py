class BankAccount:
    
    title = 'cool bank'

    def __init__(self, customer_name, current_balance, minimum_balance):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance

    def deposit(self, balance):
        self.current_balance += balance

    def withdraw(self, balance):
        self.current_balance -= balance

    def __str__(self):
        return (f"Bank: {BankAccount.title}\n"
                f"Name: {self.customer_name}\n"
                f"Balance: {self.current_balance}\n"
                f"Minimum Balance:  {self.minimum_balance}")
    
cus1 = BankAccount("Bob", 100, 10)
cus2 = BankAccount("Alice", 500, 100)

print(cus1)
print(cus2)

cus1.deposit(100)
cus2.withdraw(50)

print(cus1)
print(cus2)



