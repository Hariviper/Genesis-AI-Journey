# mini project 1
import random
is_on = True
while is_on:
    user_choice = input("do you wanna role the dice (yes/no) or you wanna quit? : ")
    if user_choice == "yes":
        dice = random.randint(1,6)
        print(f"you got : {dice}")
    elif user_choice == "quit":
        is_on = False
    else:
        print("invalid input by the user!")


# Mini project 2

numbers = ['0','1','2','3','4','5','6','7','8','9']
capital_letters = [
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
]
small_letters = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z'
]
symbols = [
    '!', '@', '#', '$', '%', '^', '&', '*',
    '(', ')', '-', '_', '=', '+',
    '[', ']', '{', '}',
    '\\', '|',
    ';', ':',
    "'", '"',
    ',', '.', '<', '>',
    '/', '?',
    '`', '~'
]


password_length = int(input("Enter the password length you want : "))

is_on = True
def word_picker(num,list,password):
    for i in range(num):
        letter = random.choice(list)
        password_list.append(letter)
    return password_list


password_list = []
final_password = " "
while is_on:
    cap_nums = random.randint(1,password_length)
    small_nums = random.randint(1,password_length)
    sym_nums = random.randint(1,password_length)
    number_nums = random.randint(1,password_length)

    combine_nums = cap_nums + small_nums + sym_nums + number_nums
    if combine_nums == password_length:
        word_picker(cap_nums,capital_letters,password_list)
        word_picker(small_nums,small_letters,password_list)
        word_picker(sym_nums,symbols,password_list)
        word_picker(number_nums,numbers,password_list)
        is_on = False

for letter in password_list:
    final_password += letter

print(final_password)


# Mini project 3
from datetime import datetime

current_date = datetime.now()
year = current_date.year

birthyear = int(input("Enter your birthyear : "))

age = year - birthyear
print(f'Your are {age} years  old.')






