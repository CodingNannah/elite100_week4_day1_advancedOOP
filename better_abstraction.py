from abc import ABC, abstractmethod
# Head First Design Patterns (OReilly) Eric Freeman - beward edition

# below are interfaces
# design interfaces!

class Duck(ABC):
    @abstractmethod
    def display(self):
        pass

class Swimmable(ABC):
    # @abstractmethod
    def swim(self):
    #     pass
        print("floats on the pond")

class Quackable(ABC):
    # @abstractmethod
    def quack(self):
    #     pass
        print("Quack!")

class Flyable(ABC):
    # @abstractmethod
    def fly(self):
    #     pass
        print("flap, flap, flap")

class Redhead(Duck, Swimmable, Quackable, Flyable):
    def display(self):
        print("I am a Redheaded Duck.")

class Mallard(Duck, Swimmable, Quackable, Flyable):
    def display(self):
        print("I am a Mallard Duck.")

class Rubberduck(Duck, Swimmable, Quackable):
    def display(self):
        print("I am a Rubber Ducky.")

    def quack(self):
        print("Squeak!") 

class Decoy(Duck, Swimmable):
    def display(self):
        print("I am a Decoy.")

    def swim(self):
        print("floats on the pond")        
