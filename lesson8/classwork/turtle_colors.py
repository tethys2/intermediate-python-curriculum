import turtle

t = turtle.Turtle()
t.speed(6)

t.pensize(4)
t.color("blue")
t.forward(100)

t.color("red")
t.left(90)
t.forward(100)

# Filling shapes
t.penup()
t.goto(-150, 0)
t.pendown()

t.color("green")
t.begin_fill()
for i in range(4):
  t.forward(80)
  t.left(90)
t.end_fill()

turtle.done()
