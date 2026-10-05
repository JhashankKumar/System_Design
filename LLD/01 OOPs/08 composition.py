"""
Composition is a design principle in object-oriented programming where a class is composed 
of one or more objects from other classes, allowing for a "has-a" relationship. This means that 
instead of inheriting from a base class, a class can contain instances of other classes as its members.

In this example, we have a `Car` class that is composed of an `Engine`, `Wheel`, and `Transmission`. 
Each of these components is represented by its own class, and the `Car` class uses instances 
of these classes to provide its functionality. This allows for better modularity and flexibility, 
as each component can be developed and maintained independently.
"""
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        print(f"Engine started with {self.horsepower} HP.")


class Wheel:
    def __init__(self, type):
        self.type = type

    def rotate(self):
        print(f"The {self.type} wheel is rotating.")


class Transmission:
    def __init__(self, type):
        self.type = type

    def shift_gear(self):
        print(f"Transmission shifted: {self.type}")


class Car:
    def __init__(self, engine, wheel, transmission):
        self.engine = engine
        self.wheel = wheel
        self.transmission = transmission

    def drive(self):
        self.engine.start()
        self.wheel.rotate()
        self.transmission.shift_gear()
        print("Car is running")


if __name__ == "__main__":
    engine = Engine(1500)
    wheel = Wheel("Alloy")
    transmission = Transmission("Automatic")

    car = Car(engine, wheel, transmission)
    car.drive()