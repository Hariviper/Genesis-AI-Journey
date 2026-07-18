# Challenge 1
word = input("enter any word : ")

char_index = 0
for char in word:
    print(f" character : {char} || character index {char_index}")
    char_index += 1


# Challenge 2
sentence = input("Enter any sentence : ").lower()
for char in sentence:
    if char == "a" or char == "i" or char == "o" or char =="e" or char == "u":
        print(char)

# Challenge 3
word = input("Enter any word : ")

word_length = len(word)
reverse_word = ""
for char in word:
    reverse_word += word[word_length-1]
    word_length += -1

print(reverse_word)

# Challenge 4

print("""
=========================
    PALINDROME CHECKER
=========================
""")

word = input("Enter any word : ")
word_length = len(word)
reverse_word = ""
for char in word:
    reverse_word += word[word_length-1]
    word_length += -1

if word == reverse_word:
    print("palindrome")
else:
    print("not palindrome")