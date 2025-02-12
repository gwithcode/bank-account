from bank import BankAccount

class savings(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.interest = 0.04
        