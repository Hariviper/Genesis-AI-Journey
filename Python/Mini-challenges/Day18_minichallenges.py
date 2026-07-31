# Mini challenge 
print("""
==============================
        FAVORITE MOVIES
==============================
""")

fav_movies = ("The conjuring","incidious","spiderman","odessy","fast 5")

print(f"""
Favorite movie among top 5 : {fav_movies[0]}
Least favorite movie : {fav_movies[-1]}
Length : {len(fav_movies)}
""")

# Mini-challenge 2
color = (120,25,0)

print(f"""
R : {color[0]}
G : {color[1]}
B : {color[2]}
""")

# Mini-challemge 3
A = set()

for users in range(10):
    user = input("Enter the name : ").lower()
    A.add(user)

print(A)

# Mini-challenge 4
programming_languages = set()
for lang in range(10):
    language = input("Enter the language : ").title()
    programming_languages.add(language)

print(programming_languages)

# Mini-challenge 5
numbers = [5,2,5,1,8,1,9,5,2]
refined_numbers = set(numbers)

print(refined_numbers)

