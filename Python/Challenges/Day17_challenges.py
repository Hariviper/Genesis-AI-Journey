# Challenge 1
print("""
=============================
      STUDENT DATABASE
=============================
""")

students = {}


for _ in range(5):
    credientials = {}
    name = input("Name:")
    credientials["age"] = int(input("Enter Age : "))
    credientials["Marks"] = int(input("Enter Marks : "))
    students[name] = credientials



for key in students.keys():
    print(f"Name : {key}")
    for key,value in students[key].items():
        print(f"{key} : {value}")
        
    

# Challenge 2
inventory = {
    "sword":10,
    "axe":5,
    "spear":2
}

print("""
===MENU====
1.Add item
2.Update Quantity
3.View Inventory
4.Exit
""")

def add(dictionary):
    item = input("what item you would like to add : ").lower()
    quantity = int(input("Quantity : "))
    dictionary[item] = quantity
    view(dictionary)

def update(dictionary):
    item = input("what item you would like to update : ").lower()
    if item in dictionary:
        quantity = int(input("Quantity : "))
        dictionary[item] += quantity
        view(dictionary)

def view(dictionary):
    for key,value in dictionary.items():
        print(f"{key} : {value}")

while True:
    try:
        choice = input("Choice : ").lower()
        
        if choice == "add item":
            add(inventory)
        elif choice == "update quantity":
            update(inventory)
        elif choice == "view inventory":
            view(inventory)
        elif choice == "exit":
            break
        else:
            if choice != "add item" or choice != "update quantity" or choice != "view inventory" or choice != "exit":
                raise ValueError("invalid input or no input!")

    except ValueError as error:
        print(f"Error : {error}")


# Challenge 3

contacts = {
    "kaju":"9373386387",
    "hidan":"9309131558",
    "dad":"9284519841"
}

def search(dictionary):
    try:
        name = input("Enter the name of contact you wanna find : ").lower()
        if name in dictionary:
            print(f"{name} : {dictionary[name]}")
        else:
            if name not in dictionary:
                raise ValueError("Contact not found!")
    except ValueError as error:
        print(f"Error : {error}")

def add(dictionary):
    name = input("enter the name of contact : ").lower()
    number = input("Enter the number : ")
    dictionary[name] = number
    print("Contact Added")

def delete(dictionary):
    try:
        name = input("Enter the name of contact you wanna delete : ").lower()
        if name in dictionary:
            dictionary.pop(name)
            print("Deleted")
        else:
            if name not in dictionary:
                raise ValueError("Contact not found")
    except ValueError as error:
        print(f"Error : {error}")

def show(dictionary):
    for key,value in dictionary:
        print(f"{key} : {value}")

print("""
1. Add Contact
2. Search Contact
3. Delete Contact
4. Show All Contacts
5. Exit
""")

while True:
    try:
        choice = input("Choice : ").lower()
        if choice == "add contact":
            add(contacts)
        elif choice == "search contact":
            search(contacts)
        elif choice == "delete contact":
            delete(contacts)
        elif choice == "show all contacts":
            show(contacts)
        elif choice == "exit":
            break
        else:
            if choice != "add contact" or choice != "search contact" or choice != "delete contact" or choice != "show all contacts" or choice != "exit":
                raise ValueError("Inavlid choice")
    except ValueError as error:
        print(f"Error : {error}")

# Challenge 4

que_ans = {
    "What is my favorite color":"black",
    "what is my age":"25",
    "who is 17 times wwe champ":"jhon cena",
    "which is the most popular finisher":"rko"
}
score = 0
questions = 0
def display_question(dictionary,score,questions):
    for key,value in dictionary.items():
        print(key)
        questions +=1
        answer = input("Answer : ").lower()
        if answer == value:
            score += 1
            print("correct")
        else:
            print(f"wrong answer the correct answer was : {value}")

    print(f"Your score is {score}/{questions}")

display_question(que_ans,score,questions)

# Bonus challenge 
   


def add_character(dictionary):
    name = input("Enter the name of character : ").lower()
    attributes = {}
    attributes["health"] = int(input("Health : "))
    attributes["attack"] = int(input("Attack power : "))
    attributes["weapon"] = input("Weapon : ").lower()
    dictionary[name] = attributes
    print("\n"*5)
    print("Added succesfully!")

def view_character(dictionary):
    choice = input("enter the name of character : ").lower()
    try:
        if choice in dictionary:
            print(f"""
                Name : {choice}
                Health : {dictionary[choice]["health"]}
                Attack : {dictionary[choice]["attack"]}
                Weapon : {dictionary[choice]["weapon"]}
                    """)
        if choice not in dictionary:
            raise ValueError("Character not found")
    except ValueError as error:
        print(f"Error : {error}")


def update_character(dictionary):
    name = input("enter the name of character : ").lower()
    try:
        if name in dictionary:
            choice = input("What would you like to update (health/attack/weapon) : ").lower()
            if choice == "health":
                dictionary[name][choice] = int(input("update health : "))
                print("\n"*5)
                print("updated!")
            elif choice == "attack":
                dictionary[name][choice] = int(input("update attack : "))
                print("\n"*5)
                print("updated!")
            elif choice == "weapon":
                dictionary[name][choice] = input("update weapon : ").lower()
                print("\n"*5)
                print("updated!")
            else:
                raise ValueError("Invalid choice!")

        if name not in dictionary:
            raise ValueError("Character not found")
    except ValueError as error:
        print(f"Error : {error}")

def delete_character(dictionary):
    name = input("Enter the name of character : ").lower()
    if name in dictionary:
        dictionary.pop(name)
        print("\n"*5)
        print("Character deleted!")

def show_characters(dictionary):
    for key in dictionary.keys():
        print(f"Name : {key}")
        for key,value in dictionary[key].items():
            print(f"{key} : {value}")


characters = {
    "mihawk": {
        "health": 100,
        "attack": 95,
        "weapon": "yoru"
    },
    "shanks": {
        "health": 100,
        "attack": 90,
        "weapon": "gryphon"
    }
}
print("""
1. Add Character
2. View Character
3. Update Character
4. Delete Character
5. Show All Characters
6. Exit
""")

print("""
        1. Add Character
        2. View Character
        3. Update Character
        4. Delete Character
        5. Show All Characters
        6. Exit
    """)
while True:
    try:
        user_choice = input("Your choice : ").lower()

        if user_choice == "add character":
            add_character(characters)
        elif user_choice == "view character":
            view_character(characters)
        elif user_choice == "update character":
            update_character(characters)
        elif user_choice == "delete character":
            delete_character(characters)
        elif user_choice == "show all characters":
            show_characters(characters)
        elif user_choice == "exit":
            break
        else:
            raise ValueError("Invalid input!")
    except ValueError as error:
        print(f'Error : {error}')