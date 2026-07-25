# Mini-challenge 1
# later i will scale it to even bigger whith loops
print("welcome to Notes app")

def watch_notes(user_file):
    with open(user_file,"r") as file:
        print(file.read())

def add_notes(user_file,note):
    with open(user_file,"a") as file:
        file.write(f"\n{note}")

def create_file(name,note):
    with open(name,"w") as file:
        file.write(note)

choice = input("type E for existing file or N for new file ").upper()

if choice == "N":
    create_file_name = input("enter the name of your new file : ").lower()
    first_note = input("Enter your first note : ")
    create_file(create_file_name,first_note)
elif choice == "E":
    existing_file = input("Enter the name of your notes file : ").lower()
    choice_two = input("do you wanna see the check the notes or add type check or add : ")
    if choice_two == "check":
        watch_notes(existing_file)
    elif choice_two == "add":
        add_new = input("enter the notes : ")
        add_notes(existing_file,add_new)
    else:
        print("invalid input")
else:
    print("You enterd wrong input.")

# Mini challenge 2
print("""
==================================
        journal Entries
==================================
""")

user_answer = input("the name of your file : ").lower()
user_choice = input("do you wanna watch the file or save something type w for watch or s to save new : ").lower()

if user_choice == "s":
    new_note = input("What did you learn today? : ")
    add_notes(user_answer,new_note)
else:
    watch_notes(user_answer)

# Mini project 2
print("""
==============================
    STUDENT RECORD MANAGER
==============================
""")

is_on = True

while is_on:

    student_name = input("Enter student name : ").title()
    student_marks = float(input("Enter student marks : "))

    with open("student_record","a") as file:
        file.write(f"\n{student_name} - {student_marks}")

    student_choice = input("do you want to exit if yes then type 'exit' or type 'no' : ").lower()
    if student_choice == "exit":
        is_on = False
    elif student_choice == "no":
        is_on = True


with open("student_record","r") as file:
    print(file.read())

    



