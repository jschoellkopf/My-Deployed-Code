class Bank_account:
    
    all_accounts = []
    
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        Bank_account.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        print(f"You now have ${self.balance}")
        return self

    def withdraw(self, amount):
        if self.balance < amount:
            print(f"not enough funds to withdraw ${amount}")
        else:
            self.balance -= amount
            print(f"You now have ${self.balance}")

        return self

    def display_account_info(self):
        print(f"{self.int_rate*100}%")
        print(self.balance)
        return self

    def yield_interest(self):
        self.balance += self.balance * self.int_rate
        print(f"You now have ${self.balance}")
        return self
    
    @classmethod
    def all_accounts_info(cls):
        for account in cls.all_accounts:
            print(f"Account's balance is {account.balance} and its interest rate is at {account.int_rate*100}%") #How to add name of account at beginning
        

damians_account = Bank_account(0.01,9463)
chandels_account = Bank_account(0.015, 54322)
jackies_account = Bank_account(0.03,20000000)

damians_account.deposit(600).deposit(1300).deposit(450).withdraw(1000).yield_interest().display_account_info()
chandels_account.deposit(4000).deposit(2500).withdraw(100).withdraw(200).withdraw(150).withdraw(250).yield_interest().display_account_info()
jackies_account.display_account_info().deposit(2).withdraw(1).yield_interest()

Bank_account.all_accounts_info()