from checking import CheckingAccount
from savings import savings

def main():
    checking = CheckingAccount("Kayd Chen", 100000, 1000)
    saving = savings("Kayd Chen", 100000, 1000, 12345, 54321)
    print("Account Information: ")
    print(checking)
    print(saving)