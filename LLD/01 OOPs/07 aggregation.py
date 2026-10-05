"""
Aggregation is a special form of association that represents a "Has-A" relationship between two classes. 
It is a way to model the relationship where one class (the whole) contains or is composed of other
classes (the parts), but the parts can exist independently of the whole.

In this example, we have a `University` class that aggregates multiple `Professor` objects. 
The `University` class can contain multiple `Professor` objects, and each `Professor` object can 
exist independently of the `University`. This allows for better organization and management of 
professors within a university, as each professor can be associated with a specific university, 
but can also exist independently of it. The aggregation relationship is established through the 
use of references, allowing for easy access and manipulation of the related objects.
"""
class Professor:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def teach(self):
        print(f"{self.name} is teaching {self.subject}")


class University:
    def __init__(self, university_name):
        self.university_name = university_name
        self.professors = []

    def add_professor(self, professor):
        self.professors.append(professor)

    def show_professors(self):
        print(f"Professor at {self.university_name}:")
        for professor in self.professors:
            print(f" - {professor.name}")


if __name__ == "__main__":
    prof1 = Professor("Dr Arnab", "Computer Science")
    prof2 = Professor("Dr Jayita", "AI")

    university = University("Jadavpur University")
    university.add_professor(prof1)
    university.add_professor(prof2)

    university.show_professors()

    # Professor can exist independently

    prof1.teach()
    prof2.teach()