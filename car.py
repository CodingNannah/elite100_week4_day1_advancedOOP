class Car():
    def __init__(self, owner, make, model, color, year):
        self.owner = owner.upper()
        self.make = make.upper()
        self.model = model.upper()
        self.color = color
        self.year = year

    # Human read:
    def __str__(self):
        return f"<Car | {self.year} {self.model}>"
    # Computer read:
    def __repr__(self):
        return f"<Car | {self.color} {self.year} {self.make} {self.model}>"

    def __eq__(self, __o):  #__o: dafault, private variable; placeholder -- could use "other"
        return self.year == __o.year

    def __lt__(self, __o):
        return self.year < __o.year

    def __gt__(self, __o):
        return self.year > __o.year

    def __le__(self, __o):
        return self.year <= __o.year

    def __ge__(self, __o):
        return self.year >= __o.year


class Car():
    def __init__(self, make, model, color, year):
        self.make = make.upper()
        self.model = model.upper()
        self.color = color.upper()
        self.year = year

    #Human readable ver
    def __str__(self):
        return f"<Car | {self.year} {self.model}>"

    #Computer readable ver
    def __repr__(self):
        return f"<Car | {self.year} {self.make} {self.model} in {self.color}>"
    
    def  __eq__(self, __o):
        return self.year == __o.year

    def __lt__(self, __o):
        return  self.year < __o.year

    def __gt__(self, __o):
        return self.year > __o.year

    def __le__(self, __o):
        return self.year <= __o.year

    def __ge__(self, __o): 
        return self.year >= __o.year

# my_car = Car("Diana", "Mazda", "CX-30", "blue" , 2019)
# kevin_car = Car("Kevin", "Mazda", "CX-5", "yellow", 2017)
# tom_car = Car("Tom","Hyndai", "Sonata", "black", 2014)
# sheryl_car = Car("Sheryl","Ford", "Fiesta", "red", 2012)
# grammy_car = Car("Sandy","Hyundai", "Elantra", "silver", 2016)
# grandpa_car = Car("Frank", "Ford", "Model T", "green", 1924)

#print(dir(my_car))

delorean = Car('Doc Brown','delorean', 'dmc-12', 'gray', 1981) # Back to the future
vw = Car('That One Guy','Volkswagon', 'Beetle', 'white', 1963) #Herbie
ford = Car('Dumb','Ford', 'Econoline', 'fluffy', 1984) #dumb and dumber
lotus = Car('Bond','Lotus', "espirit", "gray", 1982) # the spy who loved me
pontiac = Car('Michael Knight','Pontiac','Firebird', 'black', 1982) #knightrider

cars = [delorean, vw, ford, lotus, pontiac]
cars.sort()
print(cars)

print("Guess the film by car:")
for index, car in enumerate(cars):
    print(index+1, car)


#override __str__()method to mean something to the project
#override __repr__()method