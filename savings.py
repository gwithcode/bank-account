from bank import BankAccount

class savings(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.interest_rate = 0.04

    def monthy_interest(self):
        interest = self.current_balance * self.interest_rate
        self.current_balance += interest
