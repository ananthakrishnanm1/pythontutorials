import turtle
screen = turtle.Screen()
screen.bgcolor("white")
pen = turtle.Turtle()
pen.speed(10)
def draw_hexagon():
    for _ in range(6):
        pen.forward(50)
        pen.right(60)
for _ in range(10):
    draw_hexagon()
    pen.right(36)
pen.hideturtle()
turtle.done()
