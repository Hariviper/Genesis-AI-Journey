# Challenge 1
print("""
=========================
Student Attendance System
=========================
""")

students = (
    "hari",
    "douma",
    "goku",
    "kaju",
    "hidan",
    "khushu",
    "deku",
    "govind",
    "hisoka",
    "kajal"
)

for student in students:      
    name = input("Student : ").lower()
    if name in students:
        print("present.")
    else:
        print("absent")


# Challenge 2
print("""
=======================================
        Unique Lottery Numbers
=======================================
""")

numbers = set()

count = 0
for num in range(15):
    number = int(input("Enter any random number : "))
    count += 1
    numbers.add(number)

print(f"""
Total numbers enterd : {count}
Total unique numbers : {len(numbers)}
all unique numbers : {count}
""")

# Challenge 3
print("""
==============================
    COMMON FRIENDS FINDER
==============================
""")

friends_group1 = set()
friends_group2 = set()

def add_friedns(friend_set):
    for _ in range(5):
        name = input("Name of the friend : ").lower()
        friend_set.add(name)

add_friedns(friends_group1)
add_friedns(friends_group2)

common_friends = (friends_group1 & friends_group2)
print(f"""
Common friends are : {common_friends}
""")

# challenge 4
print("""
=====================================
    Movie Recommendation System
=====================================
""")

hidantv = {
    "Action",
    "Horror",
    "Comedy",
    "Sci-Fi",
    "Fantasy",
    "Anime"
}

user_genre = set()
while True:
    name = input("Input your favorite genere or type exit to exit : ").title()
    user_genre.add(name)
    if name == "Exit":
        break

recommended_genres = (hidantv & user_genre)
print(f"Recommended Genres : ")
for genre in recommended_genres:
    print(f" - {genre}")


# Bonus Inventry Challenge 
player = {
    "name":"mihawk",
    "inventory":{"conq haki","yoru","devil fruit"}

}


def add_item(dictionary):
    item_name = input("Enter the item name : ").lower()
    dictionary["inventory"].add(item_name)
    print("new Item Added")

def remove_item(dictionary):
    # try:
        item_name = input("Item name : ")
        # if item_name in dictionary:
        dictionary["inventory"].remove(item_name)
        print("Item removed")

def view_inventory(dictionary):
    print(f"Name : {dictionary["name"]}")
    print("Inventory - ")
    for item in dictionary["inventory"]:
        print(item)


print("""
1 Add Item
2 Remove Item
3 View Inventory
4 Exit
""")

while True:
    try:
        choice = input("choice : ").lower()
        if choice == "add item":
            add_item(player)
        elif choice == "remove item":
            remove_item(player)
        elif choice == "view inventory":
            view_inventory(player)
        elif choice == "exit":
            break
        else:
            raise ValueError("Invalid input!")

    except ValueError as error:
        print(f'Error : {error}')
