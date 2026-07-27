# Challenge 1
import random

print("""
==========================
Smart number Guessing game
==========================
""")

def game_logic(num,computer_guess):
    condition = num < 101 and num > 0
    
    if num > computer_guess and condition:
        return "Too high"
    elif num < computer_guess and condition:
        return "Too low"
    elif num > 100:
        return "Guess a number between 1 to 100"
    elif num == computer_guess:
        return "congratulations"
    elif num == 0:
        return "Guess a number between 1 to 100"

special_number = random.randint(1,100)
while True:
    try:
        user_guess = float(input("Guess the Number (1-100) : "))
        if user_guess < 0:
            raise ValueError("No negetive numbers choose between 1 to 100")
        print(game_logic(user_guess,special_number))

    except ValueError as error:
        print(f"Enter a valid number {error}.")

    # if game_logic(user_guess,special_number) == True:
    #     print("Congratulations")
    #     break
    if user_guess == special_number:
        break
    

# Challenge 2

print("""
======================================
       STUDENTS MARKS VALIDATOR
======================================
""")

def validator(marks):
    if marks >= 90:
        return "Grade : A"
    elif marks >= 75:
        return "Grade B"
    elif marks >=60:
        return "Grade C"
    elif marks < 60:
        return "Fail"

try:
    student_marks = float(input("Enter your marks : "))
    if student_marks < 0:
        raise ValueError("Marks cannot be Negative.")
    if student_marks > 100:
        raise ValueError("Marks cannot be Higher than 100.")
    print(validator(student_marks))
except ValueError as error:
    print(f"Error : {error}")

# note :- i finally understood the logic douma

# Challenge 3
from data import password,username
from datetime import datetime

def login_detector(file_name):              
    with open(f"Python/Challenges/{file_name}","a") as file:
        file.write(f"\nFailed Login attempt at {datetime.now()}")

def login_successful(file_name):
    with open(f"Python/Challenges/{file_name}","a") as file:
        file.write(f"\nLogin successful at {datetime.now()}")

def file_detector(file_name):
    with open(f"Python/Challenges/{file_name}","r") as file:
        file.read()


try:
    user_file = input("Enter attempt File name : ").lower()
    if user_file == "":
        raise ValueError("File name can't be empty")
    file_detector(user_file)
except FileNotFoundError:
    print(f"No such file exist")
except ValueError as error:
    print(f"Error : {error}")

else:
    
    try:
        user_username = input("Username : ").lower()
        user_password = input("Password : ")
        
        if user_username == "" and user_password == "":
            raise ValueError("Username and password cannot be empty.")
        elif user_password == "":
            raise ValueError("Password cannot be empty.")
        elif user_username == "":
            raise ValueError("username cannot be empty")

        if user_password != password and user_username != username:
            login_detector(user_file)
            raise ValueError("Incorrect password and username")
        elif user_username != username:
            login_detector(user_file)
            raise ValueError("Incorrect username")
        elif user_password != password:
            login_detector(user_file)
            raise ValueError("Incorrect password")
        

        if user_password == password and user_username == username:
            print("Login succesful")
            login_successful(user_file)
        
    except ValueError as error:
        print(f"Error : {error}")



# Challenge 4
print("""
=================================
  WELCOME TO HIDAN SAVINGS BANK
=================================
""")


def deposite(money):
    with open("Python/Challenges/banking/balance", "r") as file:
        last_balance = float(file.read())

    deposite_amount = last_balance + money
    with open("Python/Challenges/banking/balance", "w") as file:
        file.write(str(deposite_amount))

def withdraw(money):
     with open("Python/Challenges/banking/balance", "r") as file:
        last_balance = float(file.read())
     last_balance = last_balance - money
     with open("Python/Challenges/banking/balance","w") as file:
        file.write(str(last_balance))

def banking(choice,money):
    if choice == "deposite":
        deposite(money)
        print("Transaction Succesful")
    elif choice == "withdraw":
        try:
            if check_balance() < money:
                raise ValueError("Insufficient funds!")
            withdraw(money)
        except ValueError as error:
            print(f"Error : {error}")
        else:
            print("transaction Succesful")
    elif choice == "check balance":
        print(check_balance())

def check_balance():
    with open("Python/Challenges/banking/balance","r") as file:
        balance = float(file.read())
    return balance


while True:
    print("""
    Menu -
    1. Deposite
    2. Withdraw
    3. Check balance
    4. Exit
    """)

    try:
        users_choice = input("Choice : ").lower()
        if users_choice == "":
            raise ValueError("Input cannot be empty.")

        if users_choice == "exit":
            break

        if users_choice == "deposite" or users_choice == "withdraw":
            amount = float(input("Amount : "))
            if amount < 0:
                raise ValueError("Amount cannot be Negetive!")
            banking(users_choice,amount)
        elif users_choice == "check balance":
            print(f"Balance : {check_balance()}")
        else:
            if users_choice != "deposite" or users_choice != "withdraw" or users_choice != "check balance" or users_choice != "exit":
                raise ValueError("Invalid choice ! select correctly from menu.")
        
    except ValueError as error:
        print(f"Error : {error}")



   




        
