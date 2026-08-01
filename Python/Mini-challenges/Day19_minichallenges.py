# mini-challenge 1
class Warlord:
    def __init__(self):
        self.name = "Mihawk"
        self.weapon = "yoru"
        self.haki = "Conquerors"

mihawk = Warlord()
print(f"""
Name : {mihawk.name}
Weapon : {mihawk.weapon}
Haki : {mihawk.haki}
""")

# Mini challenge 2
class Car:
    def __init__(self):
        self.brand = input("Brand : ").Upper()
        self.model = input("Model : ").Upper()
        self.year = int(input("Enter Year : "))

hidan_car = Car()
kaju_car = Car()

print(f"""
First car -
Brand : {hidan_car.brand}
model : {hidan_car.model}
year : {hidan_car.year}

second car -
brand : {kaju_car.brand}
model : {kaju_car.model}
year : {kaju_car.year}
""")

# Mini-challenge - 3
class BankAccount:
    def __init__(self):
        self.owner = "Harishankar dhurve"
        self.amount = -0.03      #my actual bank balance i am broke 

account = BankAccount()

print(f"Name : {account.owner}\nAmount : {account.amount}")

# Mini-challenge -4
class Phone:
    def __init__(self):
        self.brand = input("Brand :").title()
        self.model = input("Model : ").title()
        self.battery = input("Battery : ").lower()

myphone = Phone()
print(f"""
Phone : {myphone.brand}
Model : {myphone.model}
Battery : {myphone.battery}
""")


