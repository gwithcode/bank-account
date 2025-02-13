from bank import BankAccount

class CheckingAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.limit = current_balance / 4

    """This method allows the user to transfer money from one account to another. """
    def transfer(self, amount):

        if amount <= 0:
            print("Error: amount must be positive and not 0")
        elif amount > self.limit:
            print("Error: amount exceeds transfer limit")
        elif amount > self.current_balance:
            print("Error: insufficient funds")
        else:
            self.current_balance -= amount
            print(f"Transfer successful: ${amount} transferred.")
