# print("""
# =====================================
#            BIGGEST NUMBER
# =====================================
# """)

# # taking input from user
# user_first_choice = float(input("Enter any number of your choice : "))
# user_second_choice = float(input("Enter any number of your choice : "))
# user_third_choice = float(input("Enter any number of your choice : "))

# # finding the biggest number out of user values

# biggest = user_first_choice

# if user_second_choice > biggest:
#     biggest = user_second_choice

# if user_third_choice > biggest:
#     biggest = user_third_choice


# # printig the result on screen
# print("\n"*2)
# print(f"The Biggest number is : {biggest}")


# print("""
# =======================================
#           LEAP YEAR PROGRAMME
# =======================================
# """)

# user_input = int(input("enter the Year you wanna check : "))

# if user_input % 4 == 0:
#     print(f"The year {user_input} is a Leap year") 
# else:
#     print("not leap year")



# print("""
# ==========================================
#             PASSWORD VALIDATOR
# ==========================================
# """)

# saved_password = "kajuLovesChikku69"
# user_input = input("Enter your Password :")

# if saved_password == user_input:
#     print("Access granted")
# else:
#     print("Access Denied")


print("""
=============================
    NUMBER GUESSING GAME
=============================
""")

correct_guess = 4

# taking input from user
user_guess = int(input("Guess a number between (1-10)"))

# Game logic
if user_guess == correct_guess:
    print("Congatulations you guessed it right!")
elif user_guess > correct_guess:
    print("Too High!")
elif user_guess < correct_guess:
    print("Too Low")
else:
    print("invalid input")