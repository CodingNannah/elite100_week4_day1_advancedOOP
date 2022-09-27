from abc import ABC, abstractmethod     #ABC = Abstract Base Class

class Animal(ABC):
    acc = 9.8
    def __init__(self, name, species, legs = 4):
        self.name = name
        self.species = species
        self.legs = legs
        print("making Animal")

    @abstractmethod
    def speak(self):
        pass
    
    # @abstractmethod
    def run(self):
        print("Animal Moves") # Don't do it like this use the commented way
        # pass


class Dog(Animal):
    speed = 15

    def __init__(self, is_house_trained, name, species, legs = 4):
        super().__init__(name, species, legs)
        self.is_house_trained = is_house_trained
        print("making Dog")
    
    def speak(self):
        print("BBBAAAARRRRRKKK!!!!!")

    # def run(self):
    #     print("Dog Moves")


nala = Dog(True, "Nala", "Black Lab")

nala.run()
nala.speak()