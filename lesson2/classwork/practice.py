# Problem 1
# Ask the user for a word.
# Print how many vowels it has (a, e, i, o, u).

word = input("Enter a word: ")
vowels = "aeiou"
count = 0
for ch in word.lower():
    if ch in vowels:
        count = count + 1
print("Vowels:", count)


# Problem 2
# Ask the user for a word.
# Print "Palindrome" if it reads the same backwards, otherwise print "Not palindrome".

word = input("Enter a word: ")
if word == word[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")


# Problem 3
# Ask the user for a word.
# Build a new string that contains ONLY the letters at odd indexes (1, 3, 5, ...).

word = input("Enter a word: ")
new_word = ""
for i in range(len(word)):
    if i % 2 == 1:
        new_word = new_word + word[i]
print(new_word)

# Problem 4
# Ask the user for two words.
# Print the two words combined with a dash in the middle. Example: "cat-dog".

a = input("First word: ")
b = input("Second word: ")
print(a + "-" + b)

# Problem 5
# Ask the user for a phrase.
# Build a new string that removes all spaces.

phrase = input("Enter a phrase")
result = ""
for ch in phrase:
    if ch != " ":
        result = result + ch
print(result)
