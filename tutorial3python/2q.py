import turtle
screen = turtle.Screen()
screen.bgcolor("white")
pen = turtle.Turtle()
pen.speed(5)
for _ in range(5):
    pen.forward(100)
    pen.right(72)
pen.hideturtle()
turtle.done()
