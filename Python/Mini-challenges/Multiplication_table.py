"""
====================================
Project Genesis

Multiplication Table using For Loop
====================================
"""

number = int(input("Enter a number: "))

for count in range(1,11):
    print(f"{number} x {count} = {number * count}")