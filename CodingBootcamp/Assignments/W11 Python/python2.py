class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_reward_member = False
        self.gold_card_points = 0

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
            return self
        else:
            self.is_reward_member = True
            self.gold_card_points = 200
            print(self.gold_card_points)
            # return True
            return self
    
    def spend_points(self, amount):
        if amount > self.gold_card_points:
            print(f"You are missing {abs(self.gold_card_points-amount)} point(s) to be able to do that")
            return self
        else:
            self.gold_card_points -= amount
            return self

bob = User("Bob", "Bakura", "bbakura@gmail.com", 39)
ling = User("Ling", "Woo", "lwoo@gmail.com", 97)
hugo = User("Hugo", "Pfister", "hpfister@gmail.com", 13)

bob.display_info().enroll().spend_points(50).display_info().enroll().spend_points(200)
ling.enroll().spend_points(80).display_info()
hugo.display_info().spend_points(40)
