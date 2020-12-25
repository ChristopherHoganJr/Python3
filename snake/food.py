from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        # Initialize Turtle super class
        super().__init__()
        self.shape('circle')
        self.penup()
        # Set the food to be 10x10
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        self.speed('fastest')
        self.refresh()
        

    def refresh(self):
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,260)
        self.goto(random_x, random_y)