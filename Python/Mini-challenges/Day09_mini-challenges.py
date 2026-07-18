# Mini challenge 1
print("""
=============================
        NAME FORMATTER
=============================
""")

users_name = input("Enter your full Name :")
print(users_name)
print(users_name.lower())
print(users_name.upper())
print(users_name.title())
print(len(users_name))


# Mini challenge 2
print("""
=============================
      CHARACTER COUNTER
=============================
""")

sentence = input("Enter any sentence : ").lower()

# number of character counts
# stripped_sentence = sentence.strip()
# char_count = 0
# for char in stripped_sentence:
#     char_count +=1

# other solution all in one
space_sount = 0
character_count = 0
vowel_count = 0
for char in sentence:
    if char == " ":
        space_sount += 1
    elif char != " ":
        character_count += 1

    if char == "a" or char == "i" or char == "o" or char == "e" or char == "u":
        vowel_count += 1

print(f"""
Total Number of characters = {character_count}
Number of Spaces = {space_sount}
Total vowels count = {vowel_count}
""")


print("""
==============================
      PASSWORD CHECKER
==============================
""")

stored_password = "Chikku@kaju"
user_password = input("Enter your password")
is_on = True
character = 0
uppercase_characters = 0
lowercase_character = 0

while is_on:
    if user_password != "Chikku@kaju":
        print("Access denied")
    else:
        for char in user_password:
            character += 1
            if char.upper() in user_password:
                uppercase_characters += 1
            if char.lower() in user_password:
                lowercase_character += 1
        print("Access Granted\n")
        is_on = False

if character > 8:
    print("It contains more than 8 characters")

if uppercase_characters > 0:
    print("It contains a upper case character")

if lowercase_character > 0:
    print("It contains a lower case character")




