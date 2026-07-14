"""
====================================
Project Genesis - Day 06

Guessing Game V2
====================================
"""

correct_number = 7

guess = int(input("Guess a number (1-10): "))

while guess != correct_number:

    if guess > correct_number:
        print("Too High!")

    else:
        print("Too Low!")

    guess = int(input("Try Again: "))

print("🎉 Congratulations! You guessed it!")