# Challenge 1

def increment(number):
    return number + 1

x = 10
x = increment(x)
x = increment(x)
x = increment(x)

print(x)
# it printes 13 means the each new variable x refers to a new object returned by the function

# Challenge 2

def average(numbers):
    total = 0
    count = 0
    for num in numbers:
        total += num
        count += 1

    average_of_list = total/count
    return average_of_list

def list_generator():
    user_list = []
    is_on = True
    while is_on:
        nums = input("Enter any number or type exit if you're done : ").lower()
        if nums == "exit":
            is_on = False
        else:
            user_list.append(float(nums))

    return user_list

list_of_marks = list_generator()
print(f"The average is : {average(list_of_marks)}")

# Challenge 3
def highest(numbers):
    largest = 0
    for num in numbers:
        if num > largest:
            largest = num

    return largest

list_of_numbers = list_generator()

print(f"The higest number is : {highest(list_of_numbers)}")


# Challenge 4

def student_report(marks):
    average_marks = average(marks)
    highest_marks = highest(marks)

    print(f"""
    The Highest marks : {highest_marks}
    The Average marks : {average_marks}
    """)

student_marks = list_generator()
student_report(student_marks)

    

