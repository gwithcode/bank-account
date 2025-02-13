from checking import CheckingAccount
from savings import savings

def main():
    """Creates 2 instances from each class and goes through a scenario"""
    checking = CheckingAccount("Kayd Chen", 100000, 1000, 12345, 54321)
    saving = savings("Kayd Chen", 100000, 1000, 12345, 54321)
    checking2 = CheckingAccount("Tyler Roth", 2000, 100, 6969, 9696)
    saving2 = savings("Tyler Roth", 1000, 100, 6969, 9696)
    print("Account Information: ")
    print(checking)
    print(saving)
    print("Second Account Information: ")
    print(checking2)
    print(saving2)
    print("Withdrawing 30,000 (Kayd Chen).")
    checking.withdraw(30000)
    print("Current balance after withdrawal (Kayd Chen): ", checking.current_balance)
    print("Transferring 5,000 (Kayd Chen).")
    checking.transfer(5000)
    print("Current balance after transfer (Kayd Chen): ", checking.current_balance)
    print("Applying monthly interest to savings account (Kayd Chen).")
    savings.monthly_interest(saving)
    print("Updated balance after interest (Kayd Chen): ", saving.current_balance)

if __name__ == "__main__":
    main()
