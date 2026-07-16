print("""
=======================================
        STUDENT MARKS MANAGER
=======================================
""")
# Empty list to store marks
student_marks = []

# adding marks in the list
for _ in range(5):
    user_marks = float(input("Enter your marks : "))
    student_marks.append(user_marks)

# initialising max and min to starting objects of list
max = student_marks[0]
min = student_marks[1]
total = 0
status = ""
# Finding max min and total from student marks
for marks in student_marks:
    total += marks
    if marks > max:
        max = marks
    elif marks < min:
        min = marks

# Finding average
average = total/len(student_marks)

# Addtional pass fail functionality from my side.
for marks in student_marks:
    if marks <= 33:
        status = "Fail"
    else:
        status = "Pass"


print(f"max : {max} || min : {min} || average : {average} || Marks : {student_marks} || Status : {status}")