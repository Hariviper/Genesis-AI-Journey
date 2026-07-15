# challenge 1

# for num in range(5):
#     print("*", end=" ")


# challenge 2
count = 1
for rows in range(5):
    for columns in range(1):
        print("*" * count)
        count += 1

# Challenge 3
number = int(input("Enter a number :"))

for num in range(1,number+1):
    if num % 5 == 0:
        print(num)

# challenge 4

for num in range(1,21):
    if num % 3 == 0 and num % 5 == 0:
        num = "FizzBuzz"
    elif num % 5 == 0:
        num = "Buzz"
    elif num % 3 == 0:
        num = "fizz"
    
    print(num)

    
