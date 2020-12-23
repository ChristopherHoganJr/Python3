import turtle as t
import random

arrow = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

arrow.speed('fastest')

def draw_spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        arrow.color(random_color())
        arrow.circle(100)
        arrow.setheading(arrow.heading() + size_of_gap)

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()