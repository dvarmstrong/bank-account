# Pracatice writing classes 

class BankAccount:
    accounts = []
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        

    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdrawl(self, amount):
        if (self.balance -amount) >= 0:
            self.balance -= amount
        else:
            print("insufficient funds! Charging $5 fee")
            self.balance -= 5
        return self
    
    def display_account_info(self):
        print(f"Balance:{self.balance}")
        return self

    def yield_intrest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

    @classmethod
    def print_all_accounts(cls):
        for accounts in cls.accounts:
            accounts.display_account_info()


account1 = BankAccount(.03, 1000)
account2 = BankAccount(.04, 500)

account1.deposit(100).deposit(20).deposit(50).withdrawl(200).yield_intrest().display_account_info()
account2.deposit(100).deposit(35).withdrawl(200).withdrawl(10).withdrawl(100).withdrawl(50).yield_intrest().display_account_info()
BankAccount.print_all_accounts()

