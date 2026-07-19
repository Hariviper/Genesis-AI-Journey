# Challenge 1
full_name = input("Enter your full name :").title()

surname = " "

for char in full_name:
    if char == " ":
        surname = full_name[full_name.find(" ")+1:]
        break

print(f"Your surname is : {surname}")

# Challenge 2
sentence = input("Enter any sentence of your choice: ")

uppercase_letters = ""
lowercase_letters = ""

for letter in sentence:
    if letter == letter.lower():
        lowercase_letters += letter
    else:
        uppercase_letters += letter

print(f"""
Upper case letters : {len(uppercase_letters)}
Lower case letters : {len(lowercase_letters)}
""")


# Challenge 3
word = input("Enter any word of your choice : ")

count = len(word)-1
while count >= 0:
    print(f"{word[count]} : {word.find(word[count])}")
    count -= 1


print("""
===========================
    Password checker V2
===========================
""")
# Lowercase letters
lowercase = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

# Uppercase letters
uppercase = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

# Numbers (digits)
numbers = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
]

# Common symbols
symbols = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
    '-', '_', '=', '+', '[', ']', '{', '}', '\\', '|',
    ';', ':', "'", '"', ',', '.', '<', '>', '/', '?',
    '`', '~'
]
password = input("Create a strong password : ")
has_lowercase = False
has_uppercase = False
has_numbers = False
if len(password) > 8:
    for letter in lowercase_letters:
        if letter in lowercase_letters:
            has_lowercase = True
            if letter in uppercase_letters:
                has_uppercase = True
                if letter in numbers:
                    has_numbers = True
            
else:   
    print("inavlid input")

if has_numbers == True:
    print("It has numbers")
if has_uppercase == True:
    print("It has upper case letters")
if has_lowercase == True:
    print("it has lower case letters")
if password > 8:
    print("It has more than 8 letters")
