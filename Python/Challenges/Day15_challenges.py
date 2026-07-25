
# challenge 1

def cart(item,shopping):
    with open(f"Python/Challenges/{shopping}","a") as file:
        file.write(f"\n{item}")

def show_cart(shopping):
    with open(f"Python/Challenges/{shopping}","r") as file:
        print(file.read())

is_on = True
shopping_list = "shopping_list"
while is_on:
    shopping_item = input('enter the item u like : ')
    cart(shopping_item,shopping_list)

    question = input("Do you wanna exit if yes then type yes or type no : ").lower()
    if question == 'yes':
        is_on = False

show_cart(shopping_list)

# Challenge 3
def remove_last_task(task_file):
    with open(f"Python/Challenges/{task_file}", "r") as file:
        temp_list = file.readlines()
        temp_list.remove(temp_list[-1])

    return temp_list

def refresh_list(task_file,list):
    with open(f"Python/Challenges/{task_file}", "w") as file:
        for word in list:
            file.write(word)
    

def view_task(task_file):
    with open(f"Python/Challenges/{task_file}", "r") as file:
        print(file.read())


def add(task_file,task):
    with open(f"Python/Challenges/{task_file}", "a") as file:
        file.write(task)


user_task_file = input("Enter Your task file name : ").lower()
question = input("you want to remove the task or add ? : ")

if question == "add":
    new_task = input("enter the new task : ")
    add(user_task_file,new_task)
    view_task(user_task_file)
elif question == "remove":
    new_list = remove_last_task(user_task_file)
    refresh_list(user_task_file,new_list)
    view_task(user_task_file)


# Challenge 4

from data import password, username
from datetime import datetime
is_on = True
attemps = 3
while is_on:
    user_username = input("enter your username : ").lower()
    user_password = input("enter your password")

    if password == user_password:
        print("Login succesful")
        is_on = False
    else:
        with open("Python/challenges/login-attempts.txt","a") as file:
            file.write(f"login attemp failed! {datetime.now()}\n")
            attemps -= 1
            print("wrong password!")

    if attemps == 0:
        is_on = False




    
