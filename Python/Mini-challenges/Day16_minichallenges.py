# print("""
# ===========================
#       SAFE CALCULATOR
# ===========================
# """)


# def calculator(a, b, operation):

#     if operation == "+":
#         return a + b

#     elif operation == "-":
#         return a - b

#     elif operation == "*":
#         return a * b

#     elif operation == "/":
#         return a / b

#     else:
#         raise ValueError("Invalid operation.")


# while True:

#     try:

#         value_one = float(input("Enter first number : "))
#         value_two = float(input("Enter second number : "))
#         operation = input("Choose (+,-,*,/) : ")

#         answer = calculator(value_one, value_two, operation)

#         print(f"\nAnswer : {answer}")

#     except ValueError as error:

#         print(f"Error : {error}")

#     except ZeroDivisionError:

#         print("Cannot divide by zero.")

#     choice = input("\nRun again? (yes/no): ").lower()

#     if choice == "no":
#         break


# # Mini challenge 2
# def file_explorer(file_name):
#     with open(file_name,"r") as file:
#         print(file.read())

# while True:
#     try:
#         user_file = input("Enter file : ").lower()
#         file_explorer(user_file)
#     except FileNotFoundError as error:
#         print(f"Error : {error}")


#     choice = input("do you wanna run it again (Yes or no) : ").lower()
#     if choice == "no":
#         break

# Mini challenge 3
print("""
===============================
     SECURE AGE CALCULATOR
===============================
""")
def age_checker(age_input):

    if age_input >= 18:
        return "Access Allowed"

    else:
        return "Access denied"
while True:
    try:
        age = int(input("Enter age: "))

        if age < 0:
            raise ValueError("Age cannot be negative")

        print(age_checker(age))

    except ValueError as error:
        print(error)

    choice  = input("wanna run again yes or No : ").lower()
    if choice == "no":
        break 









    