# mini project 1
user_name = input("Enter your full name : ")
def greet(name):
    print(f"Hello {name}! \nWelcome to project Genesis.")

greet(user_name)

# mini project 2
# little advanced version

def calculate(a,b,operation):
    if operation == "addition":
        return a + b
    elif operation == "substraction":
        return a - b
    elif operation == "multiplication":
        return a * b
    elif operation == "division":
        return a/b
    else:
        return "invalid input"

first_value = float(input("Enter the first value : "))
second_value = float(input("Enter the second value : "))
operation = input("choose (addition/substraction/multiplication/division)").lower()

answer = calculate(first_value,second_value,operation)

print(f"Your final answer is : {answer}")

# mini project 3 

def table(num):
    for i in range(1,11):
        answer = num * i
        print(f"{num} x {i} = {answer}")

number = int(input("Enter a number : "))
table(number)

