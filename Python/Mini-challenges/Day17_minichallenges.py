# Mini-Challenge 1
print("""
=======================
    Student Profile
=======================
""")

student_profile = {}
# student_profile["name"] = input("Enter your name :").title()
# student_profile["age"] = int(input("Enter Age : "))
# student_profile["Course"] = input("Enter Your Course : ").upper()
# student_profile["city"] = input("Enter your City : ").title()

def profile_maker(student_profile):
    student_profile["name"] = input("Enter your name :").title()
    student_profile["age"] = int(input("Enter Age : "))
    student_profile["Course"] = input("Enter Your Course : ").upper()
    student_profile["city"] = input("Enter your City : ").title()

profile_maker(student_profile)
for key,value in student_profile.items():
    print(key,value)


# Mini-challenge 2
print("""
=========================
    GAME CHARACTER
=========================
""")

def player_maker(player):
    player["Name"] = input("Enter your name :").title()
    player["Health"] = int(input("Enter health :  "))
    player["Mana"] = input("Enter Special attack: ").title()
    player["Level"] = int(input("level : "))
    player["Weapon"] = input("Enter weapon name : ").title()

mihawk = {}
player_maker(mihawk)
print(mihawk)
mihawk["Level"] += 20
mihawk["Health"] += 50
print(mihawk)

# Mini-challenge 3
print("""
Login Database
""")

data = {
    "username":"hidan@evil",
    "password":"Ihatemymind@96",
    "email":"govind6301@gmail.com"
}

try:
    user_username = input("Enter username : ").lower()
    user_password = input("Enter your password : ")

    if user_username != data["username"] or user_password != data["password"]:
        raise ValueError("Invalid username or password!")

    if user_username == data["username"]:
        if user_password == data["password"]:
            print("Login successful")

except ValueError as error:
    print(f"Error : {error}")

    

# Mini-challenge 4
def dict_creator(name):
    for _ in range(5):
        name[input("Item Name :")] = int(input('price :'))

shopping_list = {}
dict_creator(shopping_list)
print(shopping_list)

# Mini-challenge 5
def dict_creator(name):
    for _ in range(5):
        key = input("Enter student name :").title()
        name[key] = int(input('Marks :'))
    

students_marks = {}
dict_creator(students_marks)
highest = 0
total = 0

for key,value in students_marks.items():
    print(f"{key} - {value}")
    if value > highest:
        highest = value
    elif value < highest:
        lowest = value
        if value < lowest:
            lowest = value
    total += value

print(f"""
Highest - {highest}
Lowest - {lowest}
Average - {total/len(students_marks)}
""")
    
    

