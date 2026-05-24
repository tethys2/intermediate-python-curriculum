import turtle

t = turtle.Turtle()
t.speed(7)

# Move without drawing
t.penup()
t.goto(-200, 0)
t.pendown()

t.setheading(-90)
t.circle(40, 180)

t.penup()
t.goto(0, 0)
t.pendown()

# Stamping the turtle shape
t.shape("turtle")
for i in range(6):
  t.stamp()
  t.forward(50)
  t.left(60)

turtle.done()
