class Animal():
    acc = 9.8
    def __init__(self, name, species, legs = 4):
        self.name = name
        self.species = species
        self.legs = legs
        print("making Animal")

    def speak(self):
        print("Some Generic Animal Sound")
    
    def run(self):
        print("gallops")
    
# animal = Animal("Animal", "muppet", 2)
# animal.speak()
# animal.run()

# Dog extends Animal
class Dog(Animal):
    speed = 15

    def __init__(self, is_house_trained, name, species, legs = 4):
        super().__init__(name, species, legs)
        self.is_house_trained = is_house_trained
        print("making Dog")

    # Method Overriding 
    def speak(self):
        print("BAAARRKKK!!!")

    def describe(self):
        print(f"The dog has {self.speed} mph and {self.acc} m/s/**2\
acceration and is a {self.species} and is housetrained {self.is_house_trained}")

adog = Dog(True, 'Sparky', 'Lab')
print(adog.name)
print(adog.species)
print(adog.is_house_trained)
adog.speak()
adog.run()
adog.describe()

print(isinstance("hello", str))
print(isinstance("hello", int))
print(isinstance(adog, Dog))
print(isinstance(adog, Animal))

class Cat(Animal):
    speed = 12
    def __init__(self, is_litter_box_trained, name, species, legs=4):
        super().__init__(name, species, legs)
        self.is_litter_box_trained = is_litter_box_trained

    def speak(self):
        print("MEEEOOOOOOOWWW")

    def describe(self):
        print(f"The cat has {self.speed} mph and {self.acc} m/s/**2\
acceration and is a {self.species} and is housetrained {self.is_litter_box_trained}")

acat = Cat(True, "Garfield", "Calico")
acat.describe()
acat.speak()

animals = [adog, acat]

for animal in animals:
    animal.speak()
    animal.describe()

class Mutt(Dog):
    def __init__(self, second_species,  is_house_trained, name, species, legs = 4):
        super().__init__(is_house_trained, name, species, legs)
        self.second_species = second_species
        print("mutt")
        
    def describe(self):
        print(f"the is a mix of {self.species} and {self.second_species}")

tippi = Mutt("Pitbull", True, "Tippi", "Boxer")
tippi.describe()
tippi.run()
tippi.speak()

#**********************************













"""Inherit from classes in pypi!"""