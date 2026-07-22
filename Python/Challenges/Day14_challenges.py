# Challenge 1
import math 

number = int(input("Enter any number : "))
print(f"""
    The square root of {number} : {math.sqrt(number)}
    The factorial of {number} : {math.factorial(number)}
    The square of {number} : {number**2}
    """)

# Challenge 2
import my_math
print(my_math.cube(3))
print(my_math.square(5))
print(my_math.average([21,56,89,45]))


# Challenge 3
import random
print("""
==============================
    ROCK PAPER SCISSORES
==============================
""")


rock_img = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

"""
scissores_img = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

paper_img = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

def computer_draw():
    pick = random.randint(1,3)
    return pick
is_on = True
while is_on:
    user_answer = int(input("what would you like to choose (1.for rock, 2 for scissores 3 for paper) : "))
    computer_answer = computer_draw()
    if user_answer == 1 and computer_answer == 2:
        print(f"""Your choose 
            {rock_img}
            Computer choosed 
            {scissores_img}
            You win!
            """)
    elif user_answer == 2 and computer_answer == 3:
        print(f"""Your choose
            {scissores_img}
            Computer choosed 
            {paper_img}
            You win!
            """)
    elif user_answer == 3 and computer_answer == 1:
        print(f"""Your choose 
            {paper_img}
            Computer choosed 
            {rock_img}
            You win
            """)
    elif user_answer == 2 and computer_answer == 1:
        print(f"""Your choose 
            {scissores_img}
            Computer choosed
            {rock_img}
            You win!
            """)
    elif user_answer == 3 and computer_answer == 2:
        print(f"""Your choose 
            {paper_img}
            Computer choosed
            {scissores_img}
            You lose!
            """)
    elif user_answer == 1 and computer_answer == 3:
        print(f"""Your choose 
            {rock_img}
            Computer choosed 
            You LOSE!
            """)
    
    else:
        print("Invalid input")

    play_again = input("Do you wanna play again? yes or no : ").lower()
    if play_again == "no":
        is_on = False

# challenge 4

is_on = True
random_number = random.randint(1,100)
while is_on:
    
    user_guess = int(input("guess a number between 1 to 100 : "))
    if user_guess > random_number and user_guess < 101:
        print("Too High")
    elif user_guess < random_number and user_guess >= 0:
        print("Too Low")
    elif user_guess == random_number:
        print("Congratulations")
        is_on = False
    else:
        if user_guess == 6301:
            is_on = False
        else:
            print("you have to choose between 1 to 100 try again.")

    



