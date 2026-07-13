"""
=========================================
Project Genesis - Day 04

Topic: Operators

Author : Harishankar Dhurve
=========================================
"""

# -----------------------------------------
# Arithmetic Operators
# -----------------------------------------

a = 20
b = 3

print("===== Arithmetic Operators =====\n")

print(f"Addition: {a + b}")
print(f"Subtraction: {a - b}")
print(f"Multiplication: {a * b}")
print(f"Division: {a / b}")
print(f"Floor Division: {a // b}")
print(f"Modulus: {a % b}")
print(f"Power: {a ** b}")

# -----------------------------------------
# Comparison Operators
# -----------------------------------------

print("\n===== Comparison Operators =====\n")

print(f"{a} > {b} : {a > b}")
print(f"{a} < {b} : {a < b}")
print(f"{a} >= {b} : {a >= b}")
print(f"{a} <= {b} : {a <= b}")
print(f"{a} == {b} : {a == b}")
print(f"{a} != {b} : {a != b}")

# -----------------------------------------
# Boolean Arithmetic
# -----------------------------------------

print("\n===== Boolean Arithmetic =====\n")

print(f"True + True = {True + True}")
print(f"True + False = {True + False}")
print(f"False + False = {False + False}")
print(f"10 + True = {10 + True}")

# -----------------------------------------
# Type Conversion
# -----------------------------------------

print("\n===== Type Conversion =====\n")

number = "10"

print(type(number))
print(type(int(number)))

print(f"Converted Value : {int(number)}")