# "Max" -> "M-a-x-"
name = "Max"
result = ""
for ch in name:
    result = result + ch + "-"
print(result)

letters = ["p", "y", "t", "h", "o", "n"]
#dumb way
result = ""
for ch in letters:
    result = result + ch
print(result)

#smart way
built = "".join(letters)
print(built)

word = "computer"
new_word = ""
for i in range(len(word)):
    if i % 2 == 0:
        new_word = new_word + word[i]
print(new_word)
