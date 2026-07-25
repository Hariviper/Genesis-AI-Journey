"""
==========================================
PROJECT GENESIS - DAY 15

Topic : File Handling

Author : Harishankar Dhurve
==========================================
"""

# -----------------------------
# Writing to a file
# -----------------------------

with open("demo.txt", "w") as file:
    file.write("Welcome to Project Genesis!")

print("Data written successfully.")

# -----------------------------
# Reading the file
# -----------------------------

with open("demo.txt", "r") as file:
    content = file.read()

print(content)

# -----------------------------
# Appending new data
# -----------------------------

with open("demo.txt", "a") as file:
    file.write("\nDay 15 Completed")

print("Data appended successfully.")

# -----------------------------
# Reading again
# -----------------------------

with open("demo.txt", "r") as file:
    print(file.read())

# -----------------------------
# Reading line by line
# -----------------------------

with open("demo.txt", "r") as file:
    for line in file:
        print(line.strip())