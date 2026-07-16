"""
====================================
Project Genesis - Day 08

Topic : Lists

Author : Harishankar Dhurve
====================================
"""

# -------------------------------
# Creating Lists
# -------------------------------

fruits = ["Apple", "Banana", "Orange"]

numbers = [10, 20, 30, 40]

mixed = ["Harishankar", 24, True, 5.11]

print(fruits)
print(numbers)
print(mixed)

print()

# -------------------------------
# Accessing Elements
# -------------------------------

print("First Fruit :", fruits[0])
print("Second Fruit :", fruits[1])
print("Last Fruit :", fruits[-1])

print()

# -------------------------------
# Updating Elements
# -------------------------------

numbers[1] = 99

print(numbers)

print()

# -------------------------------
# Adding Elements
# -------------------------------

fruits.append("Mango")

print(fruits)

print()

# -------------------------------
# Removing Elements
# -------------------------------

fruits.remove("Banana")

print(fruits)

print()

# -------------------------------
# Length of List
# -------------------------------

print("Length :", len(fruits))

print()

# -------------------------------
# Traversing List
# -------------------------------

print("Printing every fruit")

for fruit in fruits:
    print(fruit)

print()

print("Printing indexes and values")

for index in range(len(fruits)):
    print(index, fruits[index])