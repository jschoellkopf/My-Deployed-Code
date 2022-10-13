class Pet:
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 50
    
    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self
    
    def play(self):
        self.health += 5
        return self
    
    def noise(self):
        print("pet making noise")
        return self

class Cat(Pet):
    def noise(self):
        print("Meowy-meow")
        return self
    
    def play(self):
        self.energy -= 10
        self.health += 10
        return self

class Dog(Pet):
    def noise(self):
        print("Woofy-woof")