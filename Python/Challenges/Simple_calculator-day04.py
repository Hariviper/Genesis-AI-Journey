"""
=========================================
Project Genesis - Day 04

Mini Project
Simple Calculator

Author : Harishankar Dhurve
=========================================
"""

# Taking user input

first_number = int(input("Enter first number : "))
second_number = int(input("Enter second number : "))

# Arithmetic Operations

addition = first_number + second_number
subtraction = first_number - second_number
multiplication = first_number * second_number
division = first_number / second_number
floor_division = first_number // second_number
modulus = first_number % second_number
power = first_number ** second_number

# Displaying Results

print("""
==================================
        SIMPLE CALCULATOR
==================================
""")

print(f"First Number      : {first_number}")
print(f"Second Number     : {second_number}\n")

print(f"Addition          : {addition}")
print(f"Subtraction       : {subtraction}")
print(f"Multiplication    : {multiplication}")
print(f"Division          : {division}")
print(f"Floor Division    : {floor_division}")
print(f"Modulus           : {modulus}")
print(f"Power             : {power}")