"""
=========================================
Project Genesis - Day 05

Topic: if, elif, else

Author : Harishankar Dhurve
=========================================
"""

# -----------------------------------------
# Basic if Statement
# -----------------------------------------

age = 20

if age >= 18:
    print("You are eligible to vote.")

print()

# -----------------------------------------
# if - else
# -----------------------------------------

number = 15

if number % 2 == 0:
    print(f"{number} is Even")
else:
    print(f"{number} is Odd")

print()

# -----------------------------------------
# if - elif - else
# -----------------------------------------

marks = 82

if marks >= 90:
    print("Grade A")

elif marks >= 75:
    print("Grade B")

elif marks >= 60:
    print("Grade C")

elif marks >= 40:
    print("Grade D")

else:
    print("Fail")

print()

# -----------------------------------------
# Logical Operators
# -----------------------------------------

age = 20
citizen = True

if age >= 18 and citizen:
    print("Eligible to Vote")

print()

temperature = 42

if temperature > 40 or temperature < 5:
    print("Extreme Weather")

print()

is_logged_in = False

if not is_logged_in:
    print("Please Login")