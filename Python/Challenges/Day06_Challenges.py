print("""
============================
    MULTIPLICATION TABLE
============================
""")

# taking user input
number = int(input("What numbers table you want Enter here :"))

# multiplication table logic by while loop
count = 1
while count <= 10:
    print(number*count)

    count += 1


print("""
===============================
     PASSWORD GENERATOR V2
===============================
""")

stored_password = "kajuLovesChikku@69"

user_password = input("Enter your password : ")

while stored_password != user_password:

    if user_password == stored_password:
        break
    else:
        print("Your password doesn't match")
        user_password = input("enter the password again : ")

print("Access granted")


print("""
====================================
            SUM OF NUMBERS
====================================
""")

how_many_nums = int(input("How many numbers : "))

count = how_many_nums
total = 0
while count > 0:
    user_numbers = int(input("Enter the number : "))
    total += user_numbers
    count -= 1

print(f"The total of those {how_many_nums} numbers is : {total}")