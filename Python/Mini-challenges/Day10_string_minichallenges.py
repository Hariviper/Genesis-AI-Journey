# mini project 1
print("""
==============================
     USERNAME VALIDATOR
==============================
""")

is_on = True
list_of_characters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
while is_on:
    username = input("Enter the username : ").lower()
    if len(username) > 5:
        if " " not in username:
            if username == "off":
                 is_on = False
            # for character in list_of_characters:
            #     if username.startswith(character):
            #         print("""
            #            1.Username is valid
            #            2.Username have minimun of 5 length.
            #            3.Username have no spaces.
            #            4.Username starts with a letter.    
            #         """)
            #         is_on = False
            if username[0] in list_of_characters:
                    print("""
                       1.Username is valid
                       2.Username have minimun of 5 length.
                       3.Username have no spaces.
                       4.Username starts with a letter.    
                    """)
                    is_on = False
            else:
                 print("Username doesn't starts with a letter.")

        else:
            print("No spaces allowed!.try again!")
    elif username == "off":
        is_on == False
    else:
        print("It should contain atleast 5 characters. try again!")

# mini project 2
print("""
=========================
      EMAIL CHECKER
=========================
""")

get_email = input("Enter your email : ").lower()

if ("@" in get_email) and (get_email.endswith(".com")):
     print("Valid")
else:
     print("invalid")

# Mini project 3
print("""
==========================
      Word validator 
==========================
""")

word = input("Enter any word : ")

print(f"""
First character : {word[0]}
Last character : {word[-1]}
Reverse word : {word[::-1]}
Number of vowels - 
a : {word.count("a")}
e : {word.count("e")}
i : {word.count("i")}
o : {word.count("o")}
u : {word.count("u")}

Length of the word : {len(word)}
""")