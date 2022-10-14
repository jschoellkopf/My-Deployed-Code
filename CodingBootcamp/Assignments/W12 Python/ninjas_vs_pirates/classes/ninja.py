from crypt import methods
from os import stat
import random

class Ninja:
    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")
    
    def attack( self , pirate ):
        if random.random() * self.speed > pirate.speed:
            pirate.health -= Ninja.critical_hit(self.strength)#critical hit based on speed
        else:
            pirate.health -= self.strength
        return self

    @staticmethod
    def critical_hit(base_dmg):
        return base_dmg * 2
    
