"""
Polymorphism is a concept in object-oriented programming that allows objects of different 
classes to be treated as objects of a common superclass. It enables a single interface 
to represent different underlying forms (data types). In Python, polymorphism can be 
achieved through method overriding and operator overloading.
Method overriding occurs when a subclass provides a specific implementation of a 
method that is already defined in its superclass. This allows the subclass to modify 
or extend the behavior of the inherited method. Operator overloading allows the use of 
standard operators (like +, -, *, etc.) to work with user-defined objects, enabling them to 
behave like built-in types. Polymorphism promotes code reusability and flexibility, allowing 
developers to write more generic and maintainable code. It is a key feature of object-oriented 
programming that enhances the ability to design systems that can handle different data 
types and behaviors seamlessly.
"""
class MathOperation:
    def add(self, a, b, c=0, *args):
        sumx = a + b + c
        for each in args:
            sumx += each

        return sumx


math = MathOperation()
print("Sum of 2 Numbers :", math.add(6, 7))
print("Sum of 3 Numbers :", math.add(6, 7, 9))
print("Sum of many Numbers :", math.add(6, 7, 9, 9, 7, 9, 8, 4, 8))


class Animal:
    def make_sound(self):
        print("Animal makes sound")


class Dog(Animal):
    def make_sound(self):
        print("Dog Barks")


class Cat(Animal):
    def make_sound(self):
        print("Cat Meows")


animals = [Dog(), Cat()]
for animal in animals:
    animal.make_sound()


class Car:
    def start(self):
        print("Car is Starting..")


class Bike:
    def start(self):
        print("Bike is Starting...")


# Polymorphic Function
def vehicle_start(vehicle):
    vehicle.start()


vehicle_start(Car())
vehicle_start(Bike())