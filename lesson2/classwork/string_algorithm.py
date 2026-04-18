word = "mississipi"

counts = {}
for ch in word:
    if ch in counts:
        counts[ch] = counts[ch] + 1
    else:
        counts[ch] = 1

print(counts)

# Count the vowels in a word
vowels = "aeiou"
word2 = "strawberry"
total = 0
for ch in word2:
    if ch in vowels:
        total = total + 1

print("Vowel count:", total)

# Check if a word is a plalindrome
# palindrome: front = back
test = "racecar"
if test == test[::-1]:
    print(test, "is a palindrome")
else:
    print(test, "is not a palindrome")

