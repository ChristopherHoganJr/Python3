from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
# Set screen up (width, height)
screen.setup(width=500,height=400)
# Enter a text input
user_bet = screen.textinput(title='make your bet', prompt='which turtle will in the race? Enter a color: ').lower()
colors = ['red','orange','yellow','green','blue','purple']
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for i in range(len(colors)):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-220, y=y_positions[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} is the winner!")
            else:
                print(f"You've lost! The {winning_color} is the winner!")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)
    



screen.exitonclick()