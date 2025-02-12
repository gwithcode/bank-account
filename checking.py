from bank import BankAccount


class CheckingAccount(BankAccount):

    def __init__(self, customer_name, current_balance, minimum_balance):
        