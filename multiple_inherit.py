from abc import ABC, abstractmethod

class FourLegs:         #object = noun
    def run(self):      #methods DO = verb
        print("Running on four legs.")  #properties: describe

class Furry:
    def brush(self):
        print("Brushing out fur.")

    def run(self):
        print("I have no legs. I don't run!")


class Dog(FourLegs, Furry):
    def __init__(self):
        super().__init__()


buster = Dog()
buster.run
buster.brush

"""Inherit in Correct Order"""

class Dog(Furry, FourLegs):
    def __init__(self):
        super().__init__()


buster = Dog()
buster.run
buster.brush


class Dog(Furry, FourLegs):
    def __init__(self):
        super().__init__()

    def run(self):      #overriding parent classes
        print("galloping")


buster = Dog()
buster.run
buster.brush