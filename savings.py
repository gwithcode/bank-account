from bank import BankAccount

class savings(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.annual_interest_rate = 0.04

    def monthly_interest(self):
        monthly_rate = self.annual_interest_rate/12
        interest = round(self.current_balance * monthly_rate, 2)
        self.current_balance = round(self.current_balance + interest, 2)
