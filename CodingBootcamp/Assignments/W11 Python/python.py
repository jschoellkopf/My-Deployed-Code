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

    def enroll(self):
        if self.is_reward_member == True:
            print("User already a member")
            return False # not sure why the RETURNS are important here
        else:
            self.is_reward_member = True
            self.gold_card_points = 200
            print(self.gold_card_points)
            return True
    
    def spend_points(self, amount):
        if self.gold_card_points == 0:
            print("You have no points to spend")
        elif amount > self.gold_card_points:
            print(f"You only have {self.gold_card_points} point(s) available")
            return
        else:
            self.gold_card_points -= amount

bob = User("Bob", "Bakura", "bbakura@gmail.com", 39)
ling = User("Ling", "Woo", "lwoo@gmail.com", 97)
hugo = User("Hugo", "Pfister", "hpfister@gmail.com", 13)

bob.display_info()
bob.enroll()
bob.spend_points(50)
ling.enroll()
ling.spend_points(80)
bob.display_info()
ling.display_info()
hugo.display_info()
bob.enroll()
hugo.spend_points(40)
bob.spend_points(200)