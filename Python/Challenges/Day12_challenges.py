# Challenge 1
def largest(a,b,c):
    largest = a
    if b >largest:
        largest = b

    if c > largest:
        largest = c

    return largest

a = float(input("Enter the first value : "))
b = float(input("Enter the second value : "))
c = float(input("Enter the Third value : "))
print(f"the largest value is : {largest(a,b,c)}")

# Challenge 2
def reverse(word):
    reversed_word = word[::-1]
    return reversed_word

def palindrome_checker(word):
    check_word = reverse(word)
    if check_word == word:
        return "Palindrome"
    else:
        return "Not palindrome."

user_word = input("enter any word: ")
print(f"The word is : {palindrome_checker(user_word)}")

# Challenge 3
def factorial(number):
    count = number
    factorial_of_number = 0
    for num in range(number+1):
        factorial_of_number += number *(number -1) 
        
    return factorial_of_number

user_number = int(input("Enter any number of your choosing : "))
print(f"Factorial of {user_number} is : {factorial(user_number)}")

# challenge 4
def calculate(a,b,operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a/b
    else:
        return "invalid input"


def menu():
    a = float(input("Enter the first value : "))
    b = float(input("Enter the second value : "))
    operation = input("Choose Between (+,-,*,/) :")
    result = calculate(a,b,operation)
    return result

print(f"The answer is : {menu()}")