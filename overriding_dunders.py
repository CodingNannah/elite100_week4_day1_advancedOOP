from datetime import datetime as dt
# use UTC-time: utcnow()
# dt.now() - my time
# dt.utcnow() - computer / Greenwich time
# current_time.strftime("%c") - makes human readable time
# wait to last minute to apply it!

class Person():     #overriding built-in functions
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize()
        self.age = age
        self.created_on = dt.utcnow()
        # do not create full_name here: cannot update changed names later!
        print(self.first_name, "is activated!")

    @property       # makes functions into a property
    def full_name(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        """Human readable output - should be unique!"""
        return f"<Person | {self.full_name}>"

    def __repr__(self):
        """Computer readable output - should be unique!"""
        return f"<Person | {self.last_name} {self.created_on.strftime('%c')}>"

    def __hash__(self): 
        return hash(self.full_name+self.created_on.strftime('%c'))
    # avoid hash collision!

    def __bool__(self):
        return self.age > 0

    def __del__(self):          # see how garbage collection (done using a variable) works
        print(f'Person {self.full_name} has died.')

    def __eq__(self, __o):  #__o: default, private variable; placeholder -- could use "other"
        return self.age == __o.age

    def __lt__(self, __o):
        return self.age < __o.age

    def __gt__(self, __o):
        return self.age > __o.age

    def __le__(self, __o):
        return self.age <= __o.age

    def __ge__(self, __o):
        return self.age >= __o.age


matt = Person(first_name= "matt", last_name = "leblanc", age = 53)
lisa = Person(first_name= "lisa", last_name = "kudrow", age = 55)
steve = Person(first_name= "steve", last_name = "nash", age = 55)
bambam = Person(first_name= "bambam", last_name = "rubble", age = 0)

print(matt)
print(repr(matt))
# is hashable?
print(hash("I am hashable."))
print(matt==lisa)


print('='*20)
print("Compare Steve's and Lisa's ages:")
print(steve==lisa)
print(steve>lisa)
print(steve<lisa)
print(steve<=lisa)
print(steve>=lisa)
print('='*20)
print("Compare Matt's and Lisa's ages:")
print(matt==lisa)
print(matt>lisa)
print(matt<lisa)
print(matt<=lisa)
print(matt>=lisa)
print('='*20)

people = [matt, lisa, steve, bambam]
print(people)
print(sorted(people))
print(sorted(people, reverse=True))

"""Cannot do it this way:
if Person:
    print(f"{first_name} is alive.")
else:
    print(f"{first_name} has not been born yet.")"""

# people = [matt, lisa, steve, bambam]
# for person in people:
#     if person:
#         print(f"{person.full_name} is alive")
#     else:
#         print(f"{person.full_name} has not be born yet")

