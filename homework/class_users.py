from abc import ABC, abstractmethod 
from datetime import datetime as dt

class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.created_on = dt.utcnow()

    @abstractmethod
    def email(self):
        pass

    @abstractmethod
    def id(self):
        pass

    def __str__(self):
        """Human readable output - should be unique!"""
        return f"<Users | {self.full_name}>"

    def __repr__(self):
        """Computer readable output - should be unique!"""
        return f"<Users | {self.id} {self.created_on.strftime('%c')}>"

    def __hash__(self): 
        return hash(self.first_name+self.last_name+self.created_on.strftime('%c'))

    def __eq__(self, __o):  #__o: dafault, private variable; placeholder -- could use "other"
        return self.email == __o.email


class Employee(User):
    def __init__(self, first_name, last_name, home_address, security_level, department, created_on):
        super().__init__(first_name, last_name, created_on)
        self.created_on = dt.utcnow()

    def full_name(self):
        return self.first_name + " " + self.last_name

    def email(self):
        return f'{self.first_name[0]}.{self.last_name}@company.com'

    def home_address(self):
        return (" ")

    def security_level(self):
        return (1, 2, 3, 4, 5)

    def department(self):
        return ("Customer Service", "Sales", "Marketing", "IT", "Research & Development", "Human Resources", "Accounting & Finance", "Administration & Operations")

    def __str__(self):
        """Human readable output - should be unique!"""
        return f"<Employee | {self.full_name} {self.home_address} {self.department}>"

    def __int__(self):
        """Human readable output - should be unique!"""
        return f"<Employee | {self.security_level}>"
    
    # def home_address(self, dwelling_number, street_name, city, state, zip):
    #     self.dwelling_number = dwelling_number()
    #     self.street_name = street_name()
    #     self.city = city()
    #     self.state = state()
    #     self.zip = zip()
    #     return "home_address"   
        
    def id(self):
        return f'{self.full_name}+{self.department}'
    

class Customer(User):
    def __init__(self, first_name, last_name, purchase_history, shipping_address, billing_address, created_on):
        super().__init__(first_name, last_name, created_on)
        # super(Employees.__init__(full_name))
        self.created_on = dt.utcnow()

    def full_name(self):
        return self.first_name + " " + self.last_name

    def email(self):
        return f'{self.first_name[0]}.{self.last_name}@customer.com'

    def shipping_address(self):
        return (" ")

    def billing_address(self):
        return (" ")

    def purchase_history(self):
        purchase_history = [self.purchase_history]
        return purchase_history

    # def purchase_history(self):
    #     return (self.purchase_history = [])

    def __str__(self):
        """Human readable output - should be unique!"""
        return f"<Person | {self.full_name} {self.billing_address} {self.shipping_address}>"

    # def shipping_address(self, dwelling_number, street_name, city, state, zip):
    #     self.dwelling_number = dwelling_number()
    #     self.street_name = street_name()
    #     self.city = city()
    #     self.state = state()
    #     self.zip = zip()
    #     return "shipping_address"

    # def billing_address(self, dwelling_number, street_name, city, state, zip):
    #     self.dwelling_number = dwelling_number()
    #     self.street_name = street_name()
    #     self.city = city()
    #     self.state = state()
    #     self.zip = zip()
    #     return "billing_address"

    def __eq__(self):  #__o: default, private variable; placeholder -- could use "other"
        return self.shipping_address == self.billing_address    

    def id(self):
        return f'{self.email}+{self.shipping_address}'

#+++++++++++++++++++++++++++++++++++++++++++++++++++

matt = Employee(first_name= "matt", last_name = "leblanc", home_address = "90 Bedford St, NY, NY 10014", security_level = 3, department = "Human Resources", )
ross = Employee(first_name = "ross", last_name = "geller", home_address = "17 Grove St, NY, NY 10014", security_level = 3, department = "Accounting & Finance", )
phoebe = Employee(first_name= "phoebe", last_name = "buffay", home_address = "5 Morton St, NY, NY 10015", security_level = 5, department = "Administration & Operations")

lucy = Customer(first_name= "lucy", last_name = "ricardo", shipping_address = "623 East 68th St, NY, NY 10015" , billing_address = "623 East 68th St, NY, NY 10015", purchase_history = ["fruit salad hat", "1950s vintage gloves", "1950s vintage Nicholas Reich handbag", "sound-proof earmuffs", "pearl neclace and earrings"])
ricky = Customer(first_name= "ricky", last_name = "ricardo", shipping_address = "623 East 68th St, NY, NY 10015" , billing_address = "623 East 68th St, NY, NY 10015", purchase_history = ["bongo drums", "Guayabera linen short-sleeved shirt", "Florsheim Oxfords, black", "1950s vintage Pork Pie stetson"])
cookie = Customer(first_name= "cookie", last_name = "monster", shipping_address = "123 Sesame St, NY, NY 11109" , billing_address = "123 Sesame St, NY, NY 11109", purchase_history = ["chocolate chip cookies", "macadamia nut cookies", "chocolate almond bars", "snickerdoodles", "peanut butter cookies", "Vit A&D enriched milk"])

#+++++++++++++++++++++++++++++++++++++++++++++++++++

employees = [matt, ross, phoebe]
customers = [lucy, ricky, cookie]
users = [matt, ross, phoebe, lucy, ricky, cookie]

print(users)
print(employees)
print(customers)
print(sorted(users))
print(hash("I am hashable."))


