# Challenge 1
print("""
==============================
  Top 5 Programming languages
==============================
""")

programming_languages = []
for _ in range(6):
    languages = input("Enter your favorite programming language in your order : ")
    programming_languages.append(languages)


print(f"First language : {programming_languages[0]} || Fifth language : {programming_languages[4]} || Last labguage : {programming_languages[-1]}")

# Challenge 2
numbers = []
for _ in range(10):
    user_numbers = int(input("Enter any number of your choice : "))
    numbers.append(user_numbers)

even_numbers = []
odd_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

print(f"Even Numbers : {even_numbers}\nOdd numbers : {odd_numbers}")


# Challenge 3
number_list = []
for _ in range(7):
    numbers = float(int(input("Enter any Number of your choice : ")))
    number_list.append(numbers)

max = number_list[0]
min = number_list[1]
for num in number_list:
    if num > max:
        max = num
    elif num < min:
        min = num

print(f"Numbers : {number_list}\nlargest : {max} || Smallest : {min}")

# Challenge 4
print("""
==============================
     TO-DO LIST PROGRAMME
==============================
""")
# i went with different approach this time 
task_list = []
is_on = True
while is_on:
    tasks = input("Enter the task or type to Exit to end : ").lower()
    if tasks == "exit":
        is_on = False
    else:
        task_list.append(tasks)

count = 1
for task in task_list:
    print(f"Task {count}. {task}")


# Bonus Challenge 
all_students_marks = []

for _ in range(10):
    student_marks = float(input("Enter the total marks of student :"))
    all_students_marks.append(student_marks)

highest = all_students_marks[0]
lowest = all_students_marks[1]
total_students = len(all_students_marks)
grand_total = 500
total = 0

for marks in all_students_marks:
    total += marks
    if marks > highest:
        highest = marks
    elif marks < lowest:
        lowest = marks

percentages = []

for marks in all_students_marks:
    percentage_calculation = (marks/grand_total)*100
    percentages.append(percentage_calculation)

average = total/len(all_students_marks)


num_of_passed_students = 0
num_of_failed_students = 0
for percent in percentages:
    if percent > 40:
        num_of_passed_students += 1
    else:
        num_of_failed_students +=1

print(f"""
Total Students : {total_students}
Highest Marks : {highest}
Lowest marks : {lowest}
Average Marks : {average}
Number of Student passed : {num_of_passed_students}
Number of Student failed : {num_of_failed_students}
""")