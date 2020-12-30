from turtle import Turtle

class StateLabel(Turtle):
    def __init__(self, x, y, label):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x, y)
        self.write(label)