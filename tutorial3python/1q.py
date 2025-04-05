import turtle
screen = turtle.Screen()
screen.bgcolor("white")
star = turtle.Turtle()
star.speed(5)
for _ in range(5):
    star.forward(100)
    star.right(144)
star.hideturtle()
turtle.done()
