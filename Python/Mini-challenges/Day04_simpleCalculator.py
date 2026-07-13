print("""
===================================
    WELCOME TO SIMPLE CALCULATOR
===================================
\n""")

value_one = float(input("Enter the first value : "))
Value_two = float(input("Enter the second value : "))
decision = input("what operation would you like to perfrom ADD/SUB/DIV/MULTI").upper()

if decision == "ADD":
    print(f"Output : {value_one + Value_two}")
elif decision == "SUB":
    print(f"Output : {value_one - Value_two}")
elif decision == "DIV":
    print(f"Output : {round(value_one / Value_two,2)}")
elif decision == "MULTI":
    print(f"Output : {value_one * Value_two}")
else:
    print("something went wrong")
    

