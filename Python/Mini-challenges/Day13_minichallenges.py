# mini project 1
count = 0
def greeting(name):
    global count
    count += 1
    print(f"Hello {name}.\nGreet count : {count}")


for num in range(3):
    user_name = input("Enter your name : ")
    greeting(user_name)


# mini project 2 
attempts = 3
is_on = True
stored_password = "kajuweds@chikku"
def login(password,stored_pass):
    if password == stored_pass:
        return True
    elif password != stored_password:
        global attempts
        attempts -= 1
        

def check(answer):
    global is_on
    if answer == True:
        print("Access Granted")
        is_on = False
        return is_on
    else:
        if attempts == 0:
            print("Account Locked!")
            is_on = False
            return is_on
    

while is_on:
    user_password = input("Enter your Password : ")
    answer = login(user_password,stored_password)
    check(answer)


# Mini project 3
is_on = True
def celsius_to_fahrenheit(temp):
    return round((temp * 9/5) + 32,2)

def fahrenheit_to_celsius(temp):
    return round((temp - 32) * (5/9),2)

while is_on:
    choice = input("Choose one for (C to F) type cf or (F to C) type fc : ").lower()

    if choice == "cf":
        user_temp = float(input("enter the tempreture : "))
        answer = celsius_to_fahrenheit(user_temp)
        print(f"{user_temp} C is {answer} fahrenheit.")
        
    elif choice == "fc":
        user_temp = float(input("enter the tempreture : "))
        answer = fahrenheit_to_celsius(user_temp)
        print(f"{user_temp} F is {answer} Celsius.")
    else:
        print("invaid input.")

    run_again = input("do you wanna run this programme again : ").lower()
    if run_again == "no":
        is_on = False

