# =====================================================
# GENESIS AI JOURNEY
# Day 17 Fundamentals
# Topic: Dictionaries
# =====================================================

# What is a Dictionary?

# A dictionary is a collection of data stored as KEY : VALUE pairs.

# Example:

student = {
    "name": "Harishankar",
    "age": 24,
    "course": "Python"
}

# Instead of remembering indexes like lists, dictionaries allow us to access values using meaningful keys.

# --------------------------------------------------------

# Creating a Dictionary

student = {}

# or

student = {
    "name": "Harishankar",
    "age": 24
}

# --------------------------------------------------------

# Accessing Values

student["name"]

student["age"]

# --------------------------------------------------------

# Updating Values

student["age"] = 25

student["marks"] += 5

# --------------------------------------------------------

# Adding New Keys

student["city"] = "Nagpur"

# --------------------------------------------------------

# Removing Keys

student.pop("city")

del student["city"]

# --------------------------------------------------------

# Checking if a Key Exists

if "name" in student:
    print(student["name"])

# --------------------------------------------------------

# Dictionary Methods

# .keys()

# Returns all keys.

# .values()

# Returns all values.

# .items()

# Returns both keys and values.

# Example

for key, value in student.items():
    print(key, value)

# --------------------------------------------------------

# Nested Dictionaries

students = {

    "Harishankar": {
        "Age":24,
        "Marks":95
    },

    "Rahul":{
        "Age":21,
        "Marks":81
    }

}

# Accessing

students["Harishankar"]["Marks"]

# --------------------------------------------------------

# Looping Through Dictionaries

# for key in dictionary:
#     print(key)

# for value in dictionary.values():
#     print(value)

# for key, value in dictionary.items():
#     print(key, value)

# --------------------------------------------------------

# Common Use Cases

# ✅ Student database

# ✅ Login systems

# ✅ RPG characters

# ✅ Contacts

# ✅ Inventory

# ✅ APIs (JSON)

# Almost every real-world Python application uses dictionaries.

# --------------------------------------------------------

# # Best Practices

# ✔ Use descriptive keys.

# ✔ One dictionary should represent one object.

# ✔ Use nested dictionaries when objects have multiple properties.

# ✔ Use .items() when you need both key and value.

# ✔ Use "key in dictionary" before accessing user-provided keys.

# --------------------------------------------------------

# # Things to Remember

# Lists

# Index → Value

# Example

# fruits[0]

# --------------------------------------------

# Dictionary

# Key → Value

# Example

# student["name"]

# --------------------------------------------------------

# # Professional Tip

# If you find yourself writing

# names = [...]
# ages = [...]
# marks = [...]

# it is usually a sign that a dictionary would be a better design.