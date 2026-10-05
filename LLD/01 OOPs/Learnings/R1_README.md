# Association vs Aggregation vs Composition

In Low-Level Design (LLD), **Association, Aggregation, and Composition** describe relationships between objects/classes.

They answer an important question:

> **"How are these objects related, and how strong is their ownership relationship?"**

The key difference is **ownership and lifecycle**.

| Relationship | Meaning | Ownership | Lifecycle Dependency | Example |
|---|---|---|---|---|
| Association | Objects know/use each other | No ownership | Independent | Teacher ↔ Student |
| Aggregation | Whole has parts | Weak ownership | Parts can exist independently | Department → Employees |
| Composition | Whole owns parts | Strong ownership | Parts depend on whole | House → Rooms |

---

# 1. Association

## Definition

**Association** is the most general relationship between two independent objects.

One object can **use, communicate with, or know about** another object, but neither object owns the other.

### Real-world example

A `Teacher` teaches a `Student`.

```text
Teacher ───────── Student
```

The teacher and student can exist independently.

If the teacher leaves the school, the student still exists.

If the student leaves the school, the teacher still exists.

---

## Python Example

```python
class Student:
    def __init__(self, name):
        self.name = name


class Teacher:
    def __init__(self, name):
        self.name = name

    def teach(self, student):
        print(f"{self.name} is teaching {student.name}")


student = Student("Jhashank")
teacher = Teacher("John")

teacher.teach(student)
```

### What is happening?

```text
Teacher
   |
   | uses
   ↓
Student
```

The `Teacher` does not own the `Student`.

Both objects are created independently:

```python
student = Student("Jhashank")
teacher = Teacher("John")
```

Therefore, this is **Association**.

---

## Another Example

```python
class Customer:
    def __init__(self, name):
        self.name = name


class Bank:
    def open_account(self, customer):
        print(f"Opening account for {customer.name}")


customer = Customer("Jhashank")
bank = Bank()

bank.open_account(customer)
```

The `Bank` uses the `Customer`, but it doesn't own the customer's lifecycle.

This is also **Association**.

---

# 2. Aggregation

## Definition

**Aggregation** is a specialized form of association where one object represents a **whole** and contains or manages other objects.

However, the contained objects can exist **independently** of the whole.

### Real-world example

A `Department` has `Employees`.

```text
Department
    |
    | has
    ↓
Employees
```

If the department is deleted:

```text
Department ❌
Employee   ✅
```

Employees can continue to exist and can be moved to another department.

Therefore, this is **Aggregation**.

---

## Python Example

```python
class Employee:
    def __init__(self, name):
        self.name = name


class Department:
    def __init__(self, name, employees):
        self.name = name
        self.employees = employees


employee1 = Employee("Alice")
employee2 = Employee("Bob")

employees = [employee1, employee2]

department = Department("Engineering", employees)
```

Notice that employees are created **outside** the `Department`.

```python
employee1 = Employee("Alice")
employee2 = Employee("Bob")
```

Then they are passed into the department:

```python
department = Department(
    "Engineering",
    [employee1, employee2]
)
```

The department does not control the lifecycle of the employees.

If we delete the department:

```python
del department
```

The employee objects can still exist:

```python
print(employee1.name)
print(employee2.name)
```

Therefore:

```text
Department
     ◇
     |
     ├── Employee
     └── Employee
```

The **hollow diamond (◇)** is commonly used in UML for aggregation.

---

# 3. Composition

## Definition

**Composition** is a strong form of ownership.

The child object's lifecycle is tightly coupled to the parent object.

If the parent is destroyed, the child should also be considered destroyed.

### Real-world example

A `House` contains `Rooms`.

```text
House
  |
  | owns
  ↓
Rooms
```

A room is considered part of that particular house.

If the house is destroyed, those rooms no longer exist as independent entities in that house.

Therefore:

```text
House ◆──── Room
```

The **filled diamond (◆)** represents composition in UML.

---

## Python Example

```python
class Room:
    def __init__(self, name):
        self.name = name


class House:
    def __init__(self):
        self.rooms = [
            Room("Bedroom"),
            Room("Kitchen"),
            Room("Living Room")
        ]
```

Here, the `House` creates its own rooms:

```python
class House:
    def __init__(self):
        self.rooms = [
            Room("Bedroom"),
            Room("Kitchen"),
            Room("Living Room")
        ]
```

The `Room` objects are created **inside** the `House`.

Usage:

```python
house = House()

for room in house.rooms:
    print(room.name)
```

The `House` owns its rooms.

This represents **Composition**.

---

# 4. The Most Important Difference

The easiest way to understand all three is to ask:

> **"Can the child object exist independently of the parent?"**

### Association

```text
Teacher ───── Student
```

There is no ownership.

```text
Teacher → Student
```

Both objects are independent.

---

### Aggregation

```text
Department ◇──── Employee
```

The department has employees, but employees can exist without the department.

```text
Department ❌

Employee ✅
```

---

### Composition

```text
House ◆──── Room
```

The house owns the rooms.

```text
House ❌

Room → no longer exists
```

---

# 5. Side-by-Side Python Comparison

## Association

```python
class Teacher:
    def teach(self, student):
        print(f"Teaching {student.name}")


class Student:
    def __init__(self, name):
        self.name = name


student = Student("Jhashank")
teacher = Teacher()

teacher.teach(student)
```

The objects are created independently.

---

## Aggregation

```python
class Employee:
    def __init__(self, name):
        self.name = name


class Department:
    def __init__(self, employees):
        self.employees = employees


employee1 = Employee("Alice")
employee2 = Employee("Bob")

department = Department(
    [employee1, employee2]
)
```

Employees are created outside the department.

```text
Employee lifecycle
       ↓
Independent
```

---

## Composition

```python
class Room:
    def __init__(self, name):
        self.name = name


class House:
    def __init__(self):
        self.rooms = [
            Room("Bedroom"),
            Room("Kitchen")
        ]
```

Rooms are created by the house.

```text
Room lifecycle
       ↓
Controlled by House
```

---

# 6. UML Representation

```text
Association

Teacher ───────── Student
```

```text
Aggregation

Department ◇──────── Employee
```

```text
Composition

House ◆──────── Room
```

### Symbols

```text
────────    Association

◇────────   Aggregation

◆────────   Composition
```

---

# 7. Real-World Examples

| Relationship | Example |
|---|---|
| Association | Doctor ↔ Patient |
| Association | Teacher ↔ Student |
| Association | Customer ↔ Bank |
| Association | Driver ↔ Car |
| Aggregation | Department → Employees |
| Aggregation | Team → Players |
| Aggregation | University → Professors |
| Aggregation | Library → Books |
| Composition | House → Rooms |
| Composition | Order → OrderItems |
| Composition | Car → Engine |
| Composition | BankAccount → Transactions |

> Note: Whether a relationship is aggregation or composition depends on the **domain model and lifecycle rules**, not merely on the fact that one class contains another.

---

# 8. Very Important LLD Example — Order System

Consider an e-commerce system.

```text
Order
 ├── OrderItem
 ├── OrderItem
 └── OrderItem
```

An `OrderItem` belongs to a particular order.

Example:

```python
class OrderItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        item = OrderItem(product, quantity)
        self.items.append(item)
```

Here:

```python
order.add_item(product, 2)
```

The `Order` creates the `OrderItem`.

This is a strong candidate for **Composition**.

```text
Order ◆──── OrderItem
```

However, the `Product` is different.

```text
OrderItem ──── Product
```

A product exists independently of an order.

Therefore:

```text
Order ◆──── OrderItem ──── Product
```

This is an excellent example of how **different relationships can exist in the same design**.

---

# 9. Easy Way to Remember

Think about ownership.

### Association

> **"I know/use you."**

```text
Teacher → Student
```

### Aggregation

> **"I have you, but I don't own your life."**

```text
Department ◇── Employee
```

### Composition

> **"You are a part of me, and I own your lifecycle."**

```text
House ◆── Room
```

---

# 10. Interview Question

### Question

> What is the difference between aggregation and composition?

### Answer

**Aggregation** represents a weak "has-a" relationship where the child can exist independently of the parent.

**Composition** represents a strong "has-a" relationship where the child is owned by the parent and its lifecycle is dependent on the parent.

Example:

```text
Aggregation:
Department ◇── Employee

Composition:
House ◆── Room
```

---

# 11. Quick Decision Framework

When designing an LLD system, ask these questions:

```text
                Is there a relationship?
                         |
                         ↓
                     Association
                         |
             Is there "has-a" ownership?
                    /           \
                  No             Yes
                  |               |
            Association      Can the child
                             exist independently?
                              /          \
                            Yes           No
                             |             |
                        Aggregation    Composition
```

Or simply remember:

```text
Association
    ↓
Relationship

Aggregation
    ↓
Weak ownership

Composition
    ↓
Strong ownership
```

---

# 12. Summary

| Feature | Association | Aggregation | Composition |
|---|---|---|---|
| Relationship | Yes | Yes | Yes |
| Has-a relationship | Not necessarily | Yes | Yes |
| Ownership | No | Weak | Strong |
| Child independent? | Yes | Yes | Generally no |
| Lifecycle dependent? | No | No | Yes |
| UML | `────` | `◇────` | `◆────` |
| Example | Teacher–Student | Department–Employee | House–Room |

## Golden Rule

> **Association = knows/uses**

> **Aggregation = has, but does not own**

> **Composition = owns and controls lifecycle**

---

## Practice

Try identifying the relationship in these examples:

1. `University → Students`
2. `Car → Engine`
3. `Doctor → Patient`
4. `Team → Players`
5. `Order → OrderItems`
6. `Library → Books`
7. `Bank → Customers`

For each one, ask:

> **Does the child exist independently?**

That question will usually lead you to the correct LLD relationship.