import random

# Problem 1  ( 1 : 1 )
# Ask the user for a word.
# Print the first letter and the last letter.

word = input("Enter a word: ")
print(word[0], word[-1])

# Problem 2  ( 2 : 1 )
# Ask the user for a sentence.
# Count how many vowels it has (a, e, i, o, u) and print the count.

sentence = input("Enter a sentence: ")
vowels = "aeiou"
count = 0
for ch in sentence.lower():
  if ch in vowels:
    count = count + 1
print("Vowels:", count)


# Problem 3  ( 2 : 1 )
# Use a for loop with range to print: 0, 10, 20, 30, ..., 100

for i in range(0, 101, 10):
  print(i)


# Problem 4  ( 3 : 2 )
# Ask the user for a sentence.
# Use a dictionary to count how many times each WORD appears.
# Print the dictionary.

sentence = input("Enter a sentence: ")
words = sentence.split()
freq = {}
for w in words:
  freq[w] = freq.get(w, 0) + 1
print(freq)



# Problem 5  ( 3 : 2 )
# Ask the user for a word.
# Build the reversed word WITHOUT using slicing (no [::-1]).

word = input("Enter a word: ")
rev = ""
for ch in word:
  rev = ch + rev
print(rev)

# Problem 6  ( 4 : 2 )
# Create a class called Player.
# __init__ takes name and score.
# Make a method add_points(points) that adds to the score.
# Create a Player and add points a few times, then print the final score.

class Player:
  def __init__(self, name, score):
    self.name = name
    self.score = score

  def add_points(self, points):
    self.score = self.score + points

p = Player("Ava", 0)
p.add_points(3)
p.add_points(2)
p.add_points(5)
print(p.name, "score:", p.score)

# Problem 7  ( 2 : 1 )
# Ask the user for their name and age.
# Store them in a tuple (name, age).
# Unpack the tuple into variables and print them.

name = input("Name: ")
age = int(input("Age: "))
info = (name, age)
n, a = info
print(n, a)

# Problem 8  ( 3 : 2 )
# Create a dictionary where the keys are points (x, y) stored as tuples,
# and the values are colors.
# Add at least 3 points and print the dictionary.

point_colors = {}
point_colors[(0, 0)] = "red"
point_colors[(2, 5)] = "green"
point_colors[(4, 1)] = "blue"
print(point_colors)

# Problem 9  ( 5 : 3 )
# Turtle challenge:
# Use turtle to stamp the turtle 12 times in a circle.
# Each stamp should be a random color.
# (Hint: use random.choice on a list of colors)

import turtle

t = turtle.Turtle()
t.speed(0)
t.shape("turtle")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for i in range(12):
  t.color(random.choice(colors))
  t.stamp()
  t.forward(60)
  t.left(30)
turtle.done()

# Problem 10  ( 4 : 2 )
# Ask the user for 3 student names and their scores.
# Store them in a dictionary.
# Print the name of the student with the highest score.

scores = {}
for i in range(3):
  name = input("Student name: ")
  score = int(input("Score: "))
  scores[name] = score

best_name = ""
best_score = -1
for name in scores:
  if scores[name] > best_score:
    best_score = scores[name]
    best_name = name

print("Winner:", best_name)

