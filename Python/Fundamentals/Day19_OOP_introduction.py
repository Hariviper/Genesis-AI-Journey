# ======================================================
# Genesis-AI-Journey
# Day 19 Fundamentals
# Object-Oriented Programming (Introduction)
# ======================================================

# ------------------------------------------------------
# 1. Creating a Class
# ------------------------------------------------------

class Student:
    pass


student = Student()

print(student)

# ------------------------------------------------------
# 2. Constructor (__init__)
# ------------------------------------------------------

class Student:

    def __init__(self):
        self.name = "Hari"
        self.age = 25


student = Student()

print(student.name)
print(student.age)

# ------------------------------------------------------
# 3. self
# ------------------------------------------------------

class Car:

    def __init__(self):
        self.brand = "Toyota"


car = Car()

print(car.brand)

# ------------------------------------------------------
# 4. Multiple Objects
# ------------------------------------------------------

class Dog:

    def __init__(self):
        self.name = "Tommy"


dog1 = Dog()
dog2 = Dog()

print(dog1.name)
print(dog2.name)

# ------------------------------------------------------
# 5. Changing Object Attributes
# ------------------------------------------------------

class Phone:

    def __init__(self):
        self.brand = "Oppo"


phone = Phone()

phone.brand = "Samsung"

print(phone.brand)

# ------------------------------------------------------
# Key Concepts
# ------------------------------------------------------

"""
Class
Blueprint

Object
Instance created from a class

Attribute
Data stored inside an object

__init__()
Runs automatically when an object is created

self
Represents the current object

One Class
↓

Many Objects

Object.attribute
Accesses object data
"""