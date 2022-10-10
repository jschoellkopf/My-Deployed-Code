
class Bank_account:
    
    account_id = 1
    all_accounts = []
    
    def __init__(self, int_rate, balance):
            self.int_rate = int_rate
            self.balance = balance
            self.account_id = Bank_account.account_id
            Bank_account.all_accounts.append(self)
            # Bank_account.account_id += 1

    def deposit(self, amount, acc_num):
        #for accounts in Bank_account:
        if acc_num == self.account_id:
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
        print(f"Account #{self.account_id} - Balance : ${self.balance} _ Interest rate {self.int_rate*100}%")
        return self

    def yield_interest(self):
        self.balance += self.balance * self.int_rate
        print(f"You now have ${self.balance}")
        return self
    
    @classmethod
    def all_accounts_info(cls):
        for account in cls.all_accounts:
            print(f"Account #{account.account_id} - Balance: ${account.balance} - Interest rate: {account.int_rate*100}%")


class User:
    def __init__(self, first_name, last_name, email, type_of_account):
        self.first_name = first_name
        self.last_name = last_name
        self.account = Bank_account(int_rate = 0.02, balance = 0)
        self.email = email
        self.type_of_account = Bank_account.all_accounts.append(type_of_account)

    def make_deposit(self, amount, acc_num):
        self.account.deposit(amount,acc_num)
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
        return self


bob = User("Bob", "Bakura", "bbakura@gmail.com","Checking")
# ling_c = User("Ling", "Woo", "lwoo@gmail.com")
# ling_s = User("Ling", "Woo", "lwoo@gmail.com")
#hugo = User("Hugo", "Pfister", "hpfister@gmail.com", 13)

#bob.display_info().enroll().spend_points(50).display_info().enroll().spend_points(200)
#ling.enroll().spend_points(80).display_info()
#hugo.display_info().spend_points(40)

bob.make_deposit(400,2)
# ling.make_deposit(400,3)

# print(Bank_account)
# print(bob)
# print(ling)
Bank_account.all_accounts_info()
