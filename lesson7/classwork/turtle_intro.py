import turtle

t = turtle.Turtle()  # initialize turtle
t.speed(3)           # set turtle speed

t.forward(100)  # move forward
t.left(90)      # turn left
t.forward(100)

t.right(90)  # turn right
t.forward(50)

# Pen control
t.penup()
t.forward(50)
t.pendown()
t.forward(50)

turtle.done()
