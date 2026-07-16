
print("""
==============================
Mini challenge - shopping list
==============================
""")
# creating a empty list to store items
shopping_list = []

# logic to add items
while True:
    items = input("Enter the item or type done to finish : ")
    shopping_list.append(items)

    if items == "done":
        break

for item in shopping_list:
    print(item)

# my alternate way of printing

print(f"""the length of the shopping list is {len(shopping_list)}\n
The items are : {shopping_list}      
""")


print("""
==========================
       FAVORITE MOVIE
==========================
""")

favorite_movies = []

for _ in range(5):
    movies = input("Enter you favorite movie by your order : ")
    favorite_movies.append(movies)

print(f"First Movie : {favorite_movies[0]}, Last movie : {favorite_movies[-1]}")
count = 1
for movie in favorite_movies:
    print(f"movie {count} : {movie}")
    count += 1