# class RetirementAccount(BankAccount):
#     def __init__(self, int_rate, is_roth, balance=0):
#         self.int_rate = int_rate
#         self.balance = balance
#         self.is_roth = is_roth  

class RetirementAccount(BankAccount):
    def __init__(self, int_rate, is_roth, balance=0):
        super().__init__(int_rate, balance)	
        self.is_roth = is_roth	


class BankAccount:
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance
    
#--------------------------------------

# class RetirementAccount(BankAccount):
#     def withdraw(self, amount, is_early):
#         if is_early:
#     	    amount = amount * 1.10
#         if (self.balance - amount) > 0:
#             self.balance -= amount
#         else:
#             print("INSUFFICIENT FUNDS")
#         return self

class RetirementAccount(BankAccount):
    def withdraw(self, amount, is_early):
        if is_early:
    	    amount = amount * 1.10
        super().withdraw(amount)
        return self

class BankAccount:
    def withdraw(self, amount):
        if (self.balance - amount) > 0:
            self.balance -= amount
        else:
            print("INSUFFICIENT FUNDS")
        return self
    
    
# ____________________ OVERRIDING
class Parent:
    def method_a(self):
        print("invoking PARENT method_a!")
class Child(Parent):
    def method_a(self):
        print("invoking CHILD method_a!")
dad = Parent()
son = Child()
dad.method_a()
son.method_a() # this overrides the Parent method!

# _____________________ POLYMORPHISM
# We'll use the Person class to demonstrate polymorphism
# in which multiple classes inherit from the same class but behave in different ways

class Person:
    def pay_bill(self):
        raise NotImplementedError
# Millionaire inherits from Person
class Millionaire(Person):
    def pay_bill(self):
        print("Here you go! Keep the change!")
# Grad Student also inherits from the Person class
class GradStudent(Person):
    def pay_bill(self):
        print("Can I owe you ten bucks or do the dishes?")

