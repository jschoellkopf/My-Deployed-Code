import math

class Pirate:
    def __init__( self , name ):
        self.name = name
        self.strength = 14
        self.speed = 3
        self.health = 100

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack ( self , ninja ):
        if self.health < 20:
            ninja.health -= Pirate.rampage(self.strength) #increased damage when low HP
        else:
            ninja.health -= self.strength
        return self

    @staticmethod
    def rampage(base_dmg):
        return math.floor(base_dmg * 1.2)

class Blackbeard(Pirate):
    def __init__(self, name):
        super().__init__(name)
        self.strength = 16
    
    def attack(self, ninja):
        super().attack(ninja)
        if ninja.health < 10:
            ninja.health = 0 #execute if under 5HP
        return self