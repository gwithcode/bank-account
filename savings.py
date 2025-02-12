from bank import BankAccount

class savings(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.annual_interest_rate = 0.04

    def monthy_interest(self):
        monthy_rate = self.annual_interest_rate/12
        interest = self.current_balance * monthy_rate
        self.current_balance += interest
