
class Bank_account:
    
    account_id = 1
    all_accounts = []
    
    def __init__(self, int_rate, balance):
        if input("what kind of account would you like to create? type C for checking and S for savings") == "C":
            self.account_type = "Checking Account"
            self.int_rate = int_rate
            self.balance = balance
            self.account_id = Bank_account.account_id
            Bank_account.all_accounts.append(self)
        else:
            self.account_type = "Savings Account"
            self.int_rate = int_rate
            self.balance = balance
            self.account_id = Bank_account.account_id
            Bank_account.all_accounts.append(self)
        Bank_account.account_id += 1

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
        print(f"Account #{self.account_id} - Type: {self.account_type} - Balance : ${self.balance} _ Interest rate {self.int_rate*100}%")
        return self

    def yield_interest(self):
        self.balance += self.balance * self.int_rate
        print(f"You now have ${self.balance}")
        return self
    
    @classmethod
    def all_accounts_info(cls):
        for account in cls.all_accounts:
            print(f"Account #{account.account_id} - Type: {account.account_type} - Balance: ${account.balance} - Interest rate: {account.int_rate*100}%")
            #print(f"Account number #{account.account_id}, the balance is ${account.balance} and its interest rate is at {account.int_rate*100}%") #How to add name of account at beginning

#damians_account = Bank_account(0.01,9463)
#chandels_account = Bank_account(0.015, 54322)
#jackies_account = Bank_account(0.03,20000000)

#damians_account.deposit(600).deposit(1300).deposit(450).withdraw(1000).yield_interest().display_account_info()
#chandels_account.deposit(4000).deposit(2500).withdraw(100).withdraw(200).withdraw(150).withdraw(250).yield_interest().display_account_info()
#jackies_account.display_account_info().deposit(2).withdraw(1).yield_interest()

#Bank_account.all_accounts_info()

class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.account = Bank_account(int_rate = 0.02, balance = 0)
        self.email = email
        self.age = age
        self.is_reward_member = False
        self.gold_card_points = 0

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        print(f"Your balance is ${self.account.balance}")
        return self

    def show_account_info(self):
        self.account.display_account_info()
        return self

    def add_interest(self):
        self.account.yield_interest()
        return self

    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_reward_member)
        print(self.gold_card_points)
        return self

    def enroll(self):
        if self.is_reward_member == True:
            print("User already a member")
            # return False # not sure why the RETURNS are important here
        else:
            self.is_reward_member = True
            self.gold_card_points = 200
            print(self.gold_card_points)
            # return True
        return self
    
    def spend_points(self, amount):
        if amount > self.gold_card_points:
            print(f"You are missing {abs(self.gold_card_points-amount)} point(s) to be able to do that")
        else:
            self.gold_card_points -= amount
        return self

bob = User("Bob", "Bakura", "bbakura@gmail.com", 39)
ling = User("Ling", "Woo", "lwoo@gmail.com", 97)
ling = User("Ling", "Woo", "lwoo@gmail.com", 97)
#hugo = User("Hugo", "Pfister", "hpfister@gmail.com", 13)

#bob.display_info().enroll().spend_points(50).display_info().enroll().spend_points(200)
#ling.enroll().spend_points(80).display_info()
#hugo.display_info().spend_points(40)

bob.make_deposit(400).make_withdrawal(30).show_account_info()
ling.display_user_balance().make_withdrawal(20).make_deposit(200).make_withdrawal(20)

Bank_account.all_accounts_info()
