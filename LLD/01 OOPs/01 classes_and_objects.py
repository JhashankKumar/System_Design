"""
Class and Object in Python
Class is a blueprint for creating objects. An object has properties and methods(functions) 
associated with it. Almost everything in Python is an object, with its properties and methods.
"""

class Car:
    # Constructor
    def __init__(self, color, make, model, year):
        self.color = color
        self.make = make
        self.model = model
        self.year = year

    # Method to display car Details
    def display_info(self):
        print(f"Car Color: {self.color}")
        print(f"Car Make: {self.make}")
        print(f"Car Model: {self.model}")
        print(f"Car Year: {self.year}")


car1 = Car("Red", "Maruti", "Alto", "2015")
car2 = Car("Grey", "TATA", "Altroz", "2023")

# Displaying information of each car
car1.display_info()
print("------------")
car2.display_info()