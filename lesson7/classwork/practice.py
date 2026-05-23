# Problem 1
# Use turtle to draw a square with side length 80.

import turtle
t = turtle.Turtle()
t.speed(6)

for i in range(4):
  t.forward(80)
  t.left(90)

# Problem 2
# Use turtle to draw a rectangle with width 120 and height 60.

t.penup()
t.goto(-200, 0)
t.pendown()

for i in range(2):
  t.forward(120)
  t.left(90)
  t.forward(60)
  t.left(90)

# Problem 3
# Use turtle to draw a hexagon (6 sides).
# Each side should be length 70.

t.penup()
t.goto(0, -150)
t.pendown()

for i in range(6):
  t.forward(70)
  t.left(60)

# Problem 4
# Use turtle to draw a simple house:
# - A square for the base
# - A triangle roof on top

t.penup()
t.goto(200, -50)
t.pendown()

for i in range(4):
  t.forward(80)
  t.left(90)

t.left(90)
t.forward(80)
t.right(90)

for i in range(3):
  t.forward(80)
  t.left(120)

# Problem 5
# Use turtle to draw a circle with radius 50.

t.penup()
t.goto(-50, 150)
t.pendown()
t.circle(50)

turtle.done()
