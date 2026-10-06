"""
Inheritance is a fundamental concept in object-oriented programming (OOP) 
that allows a class (called a child or subclass) to inherit properties and methods 
from another class (called a parent or superclass). 

This promotes code reusability and establishes a hierarchical relationship between classes.
In Python, inheritance is implemented by defining a new class that derives from an existing class. 
The child class can override or extend the functionality of the parent class. Python supports 
multiple inheritance, allowing a child class to inherit from more than one parent class. 
However, care must be taken to avoid ambiguity and maintain clarity in the class hierarchy. 
The `super()` function is often used to call methods from the parent class, 
enabling the child class to access and utilize the functionality of its ancestors.

"""

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating...")


class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking...")

    def eat(self):
        super().eat()
        print(f"{self.name} is eating bones...")

class Indian_Dog(Dog):
    def bark(self):
        print(f"{self.name} is barking...")

    def eat(self):
        print(f"{self.name} is eating rice...")

class Labrador(Dog):
    def bark(self):
        print(f"{self.name} is barking...")

    def eat(self):
        print(f"{self.name} is eating meat...")

class MyDog(Indian_Dog, Labrador):
    def passing(self):
        pass



if __name__ == "__main__":
    my_dog = MyDog("Motu")
    my_dog.eat()
    my_dog.bark()