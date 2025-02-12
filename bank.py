class BankAccount:
    
    title = 'cool bank'

    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance
        self._account_number = account_number
        self.__routing_number = routing_number

    def deposit(self, balance):
        self.current_balance += balance

    def withdraw(self, balance):
        self.current_balance -= balance

    def getRouting(self):
        return self.__routing_number    #return routing number    

    def __str__(self):
        return (f"Bank: {BankAccount.title}\n"
                f"Name: {self.customer_name}\n"
                f"Balance: {self.current_balance}\n"
                f"Minimum Balance:  {self.minimum_balance}"
                f"Account Number: {self._account_number}")