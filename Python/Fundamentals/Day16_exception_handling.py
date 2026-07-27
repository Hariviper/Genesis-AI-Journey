"""
=========================================
PROJECT GENESIS - DAY 16

Topic: Exception Handling

Author: Harishankar Dhurve
=========================================
"""

# -----------------------------
# ValueError
# -----------------------------

try:
    number = int(input("Enter a number: "))
    print(number)

except ValueError:
    print("Invalid number!")

# -----------------------------
# ZeroDivisionError
# -----------------------------

try:
    a = float(input("First number: "))
    b = float(input("Second number: "))

    print(a / b)

except ZeroDivisionError:
    print("Cannot divide by zero.")

# -----------------------------
# FileNotFoundError
# -----------------------------

try:
    with open("unknown.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("File not found.")

# -----------------------------
# else and finally
# -----------------------------

try:
    age = int(input("Age: "))

except ValueError:
    print("Invalid input.")

else:
    print(f"Age is {age}")

finally:
    print("Program ended.")