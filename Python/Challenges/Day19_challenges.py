# challenge 1
class AnimeCharacter:
    def __init__(self):
        self.name = input("Enter Name : ")
        self.weapon = input("Enter weapon : ")
        self.power = input("Power : ")
        self.anime = input("Anime : ")

character_one = AnimeCharacter()
character_two = AnimeCharacter()
character_three = AnimeCharacter()

print(f"""
character 1 :
name : {character_one.name}
weapon : {character_one.weapon}
power : {character_one.power}
anime: {character_one.anime}

character 2
name : {character_two.name}
weapon : {character_two.weapon}
power : {character_two.power}
anime: {character_two.anime}

Character 3
name : {character_three.name}
weapon : {character_three.weapon}
power : {character_three.power}
anime: {character_three.anime}
""")

# Challenge 2
class Movie:
    def __init__(self):
        self.title = input("Title : ").title()
        self.rating = float(input("Rating : "))
        self.year = int(input("Year : "))

movie1 = Movie()
movie2 = Movie()
movie3 = Movie()
movie4 = Movie()
movie5 = Movie()

list_of_movies  = [movie1,movie2,movie3,movie4,movie5]

for movie in list_of_movies:
    print(f"""
    Title : {movie.title}
    ratings : {movie.rating}
    year : {movie.year}
    """)

# Challenge 3
class Employee:
    def __init__(self):
        self.name = input("Employee Name : ").title()
        self.company = input("Company : ").title()
        self.salary = float(input("Salary : "))

employee_one = Employee()
employee_two = Employee()
employee_three = Employee()

list_of_employees = [employee_one,employee_two,employee_three]

for employee in list_of_employees:
    print(f"""
    Name : {employee.name}
    Company : {employee.company}
    Salary : {employee.salary}
    """)

# Challenge 4
class AIengineer:
    def __init__(self):
        self.name = input("Name : ").title()
        self.skills = self.add_skills()
        self.experience = input("Experience : ")
        self.preferrd_language = input("Preferred language : ").title()
        self.dream_company = input("Dream company : ")
        self.github = input("Git hub : ")

    def add_skills(self):
        self.list_of_skills = []
        while True:
            skill = input("Enter skill or type exit : ").title()
            self.list_of_skills.append(skill)

            if skill == "Exit":
                break
        return self.list_of_skills


myself = AIengineer()

print(f"""
Name : {myself.name}
Skills : {myself.skills}
Experience : {myself.experience}
Preferrd Language : {myself.preferrd_language}
Dream company : {myself.dream_company}
Git Hub : {myself.github}
""")

# Bonus Challenge 
class OnePeice:
    def __init__(self):
        self.name = input("Name : ").title()
        self.swordsmen = input("Swordsmen yes or no : ").title()
        self.haki = input("haki : ").title()
        self.devil_fruit = input("Devil fruit : ").title()
        self.nickname = input("Nickname : ").title()
        self.bounty = float(input("Bounty : "))

character_one = OnePeice()
character_two = OnePeice()
character_three = OnePeice()

list_of_characters = [character_one,character_two,character_three]
for character in list_of_characters:
    print(f"""
Name : {character.name}
Swordsmen : {character.swordsmen}
Haki : {character.haki}
Devil fruit : {character.devil_fruit}
Nickname : {character.nickname}
Bounty : {character.bounty}
""")
    