import turtle as t
import random

t.colormode(255)
paintBrush = t.Turtle()
paintBrush.speed('fastest')
paintBrush.penup()
paintBrush.hideturtle()

# Extracted colors using color_extractor.py
color_list = [(131, 166, 205), (222, 148, 106), (31, 42, 61), (199, 134, 147), (165, 59, 48), (140, 184, 162), (39, 105, 157), (238, 212, 89), (152, 58, 66), (217, 81, 70), (169, 29, 33), (236, 165, 156), (50, 112, 90), (35, 61, 55), (17, 97, 71), (156, 33, 30), (231, 160, 165), (53, 44, 49), (170, 188, 221), (57, 51, 48), (189, 100, 110), (31, 60, 109), (103, 127, 161), (34, 151, 209), (174, 200, 188), (65, 66, 56)]

paintBrush.setheading(225)
paintBrush.forward(500)

paintBrush.setheading(0)

number_of_dots = 100
for i in range(1, number_of_dots + 1):
    paintBrush.dot(20, random.choice(color_list))
    paintBrush.forward(75)
    
    if i % 10 == 0:
        paintBrush.setheading(90)
        paintBrush.forward(75)
        paintBrush.setheading(180)
        paintBrush.forward(750)
        paintBrush.setheading(0)


screen = t.Screen()
screen.exitonclick()