# mini challenge 1
def percentage(marks):
    percentage_obtained = (marks/500)*100
    return percentage_obtained

def grade(percent):
    if percent >= 90:
        return "Grade A"
    elif percent >= 75:
        return "Grade B"
    elif percent >= 60:
        return "Grade C"
    else:
        return "Fail"

    
marks_recieved = float(input("Enter your marks recieved out of 500 : "))
result = grade(percentage(marks_recieved))
print(f"The Result is : {result}")

# mini project 2
circle_radius = float(input("Enter the radius of the circle: "))

def area(radius):
    circle_area = 3.14*(radius**2)
    return circle_area

print(f"circle area is : {area(circle_radius)}")

# Mini project 3
def discount(price,percent):
    discount_amount = price * (percent*0.01)
    final_price = price - discount_amount
    return final_price

total_price = float(input("Enter the total price : "))
discount_given = float(input("Enter the discount recieved in % : "))
print(f"the amount after discount is : {discount(total_price,discount_given)}")
