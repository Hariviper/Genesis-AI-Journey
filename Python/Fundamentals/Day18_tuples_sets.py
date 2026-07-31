# =====================================================
# Genesis-AI-Journey
# Day 18 - Tuples & Sets Fundamentals
# =====================================================

# =====================================================
# TUPLES
# =====================================================

# Creating a tuple
movies = ("The Conjuring", "Insidious", "Fast Five")

print(movies)

# Accessing elements
print(movies[0])      # First element
print(movies[-1])     # Last element

# Length
print(len(movies))

# Tuples are immutable
# movies[0] = "Avengers"   # ❌ TypeError


# =====================================================
# SETS
# =====================================================

# Creating a set

languages = {"Python", "Java", "Python", "C++"}

print(languages)
# Output:
# {'Python', 'Java', 'C++'}


# Empty set
skills = set()

skills.add("Python")
skills.add("Java")
skills.add("Python")

print(skills)


# Removing values

skills.remove("Java")

# Safe removal (doesn't crash if item doesn't exist)
skills.discard("HTML")

print(skills)


# Membership

if "Python" in skills:
    print("Python Found")


# =====================================================
# SET OPERATIONS
# =====================================================

A = {"Python", "Java", "C++"}
B = {"Java", "C#", "Python"}

# Union
print(A | B)

# Intersection
print(A & B)

# Difference
print(A - B)

# Difference
print(B - A)


# =====================================================
# REMOVE DUPLICATES
# =====================================================

numbers = [1, 2, 2, 3, 4, 4, 5]

unique_numbers = set(numbers)

print(unique_numbers)


# =====================================================
# TUPLE EXAMPLES
# =====================================================

rgb = (255, 120, 50)

print(rgb[0])
print(rgb[1])
print(rgb[2])


coordinates = (18.5204, 73.8567)

print(coordinates)


# =====================================================
# REAL WORLD EXAMPLES
# =====================================================

# Inventory

inventory = {"Sword", "Shield", "Potion"}

inventory.add("Bow")

inventory.discard("Potion")

print(inventory)


# Student IDs

student_ids = {101, 102, 103, 101, 102}

print(student_ids)


# Completed Quests

completed_quests = {
    "Dragon Slayer",
    "Forest Rescue",
    "Dragon Slayer"
}

print(completed_quests)


# =====================================================
# Choosing the Right Data Structure
# =====================================================

# List
shopping = ["Milk", "Eggs", "Bread"]

# Tuple
months = (
    "Jan", "Feb", "Mar", "Apr",
    "May", "Jun", "Jul", "Aug",
    "Sep", "Oct", "Nov", "Dec"
)

# Set
languages = {"Python", "Java", "C++"}

# Dictionary
player = {
    "name": "Mihawk",
    "health": 100,
    "weapon": "Yoru"
}


# =====================================================
# Notes
# =====================================================

# List
# Ordered
# Mutable
# Allows duplicates

# Tuple
# Ordered
# Immutable

# Set
# Unordered
# Mutable
# No duplicates

# Dictionary
# Key-Value pairs
# Fast lookup
# Best for modelling real-world objects