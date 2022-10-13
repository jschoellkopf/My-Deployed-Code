import pet

class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
    
    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        self.pet.eat()
        return self
    
    def bathe(self):
        self.pet.noise()
        return self

ryan = Ninja("Ryan", "Boder", "chewies", "meat", pet.Dog("Bood", "border-colis", "high-five"))
# how do I add another pet to ryan, should it be in the constructor, making a cat and a dog instead of a pet, but then how do you walk or bathe a specific pet?

print(ryan.pet.energy, ryan.pet.health)
ryan.feed().walk().bathe()
print(ryan.pet.energy, ryan.pet.health)


# class Ninja:
#     def __init__(self, first_name, last_name, treats, pet_food, dog, cat):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.treats = treats
#         self.pet_food = pet_food
#         self.dog = dog
#         self.cat = cat
    
#     def walk(self):
#         self.dog.play()
#         return self

#     def feed(self):
#         self.dog.eat()
#         return self
    
#     def bathe(self):
#         self.dog.noise()
#         return self

# ryan = Ninja("Ryan", "Boder", "chewies", "meat", pet.Dog("Bood", "border-colis", "high-five"), pet.Cat("Batman","bobtail","catching flies"))

# print(ryan.dog.energy, ryan.dog.health, ryan.cat.energy, ryan.cat.health)
# ryan.feed().walk().bathe()
# ryan.feed().walk().bathe()
# print(ryan.dog.energy, ryan.dog.health, ryan.cat.energy, ryan.cat.health)
