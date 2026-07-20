# Challenge 1
def largest(a,b,c):
    large = a
    if b > large:
        large = b
    if c > large:
        large = c

    return large

first_value = float(input("Enter the first value : "))
second_value = float(input("Enter the second value : "))
third_value = float(input("Enter the third value : "))

print(f"The largest value : {largest(first_value,second_value,third_value)}")

# challenge 2 

def count_vowels(word):
    print(f"""
    vowel a count : {word.count("a")}
    vowel e count : {word.count("e")}
    vowel i count : {word.count("i")}
    vowel o count : {word.count("o")}
    vowel u count : {word.count("u")}
    """)

random_word = input("Enter any word of your choice : ").lower()
count_vowels(random_word)

# Challenge 3

def reverse(word):
    reversed_word = " "
    count = len(user_word)-1
    while count >= 0:
        reversed_word += user_word[count]
        count += -1

    return reversed_word

user_word = input("Enter any word of your choice : ").lower()
print(f"Reversed word : {reverse(user_word)}")


# Challenge 4
def reverse(word):
    reversed_word = " "
    count = len(word)-1
    while count >= 0:
        reversed_word += word[count]
        count += -1

    if word == reversed_word:
        print("Palindrome.")
    else:
        print("Not palindrome.")

user_word = input("Enter any word of your choice : ").lower()

reverse(user_word)