# Problem 1
# Use turtle to draw a filled triangle (any color).

import turtle
t = turtle.Turtle()
t.speed(7)

t.penup()
t.goto(-30, 70)
t.pendown()

t.color("purple")
t.begin_fill()
for i in range(3):
  t.forward(120)
  t.left(120)
t.end_fill()

# Problem 2
# Use turtle to draw a circle, then move and draw another circle.
# Make the circles different colors.

t.penup()
t.goto(-200, 0)
t.pendown()
t.color("blue")
t.circle(50)

t.penup()
t.goto(-20, 0)
t.pendown()
t.color("red")
t.circle(30)

# Problem 3
# Use turtle to stamp the turtle 8 times in a circle (like a clock).
# (Hint: stamp, forward, turn)

t.penup()
t.goto(0, -170)
t.pendown()
t.shape("turtle")
t.color("green")

for i in range(8):
  t.stamp()
  t.forward(60)
  t.left(45)

# Problem 4
# Use turtle to draw a square spiral:
# Start with length 20.
# Each time, increase length by 10.

t.penup()
t.goto(-150, -150)
t.pendown()
t.color("black")

length = 20
for i in range(12):
  t.forward(length)
  t.left(90)
  length = length + 10

# Problem 5
# Use turtle to draw a smiley face:
# - Big circle for head
# - Two small circles for eyes
# - A curved mouth (part of a circle)

t.penup()
t.goto(160, -50)
t.pendown()
t.color("orange")
t.circle(80)

t.penup()
t.goto(130, 40)
t.pendown()
t.color("black")
t.circle(10)

t.penup()
t.goto(190, 40)
t.pendown()
t.circle(10)

t.penup()
t.goto(110, -10)
t.pendown()
t.setheading(-60)
t.circle(60, 120)

turtle.done()
