from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.tracer(0)
# Add starting and finish line
screen.register_shape('race_line', ((-150, 2), (-150,-2), (150,-2), (150,2)))

# Set screen up (width, height)
screen.setup(width=1000,height=400)
screen.title('PyRacing - Turtle Racing')
# Starting Line
starting_line = Turtle(shape='race_line')
starting_line.hideturtle()
starting_line.penup()
starting_line.setx(-450)

# Finish Line
finish_line = Turtle(shape='race_line')
finish_line.hideturtle()
finish_line.penup()
finish_line.setx(450)

starting_line.showturtle()
finish_line.showturtle()

screen.update()

# Enter a text input
user_bet = screen.textinput(title='make your bet', prompt='which turtle will in the race? Enter a color: ').lower()
colors = ['red','orange','black','green','blue','purple']
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

screen.tracer(True)
for i in range(len(colors)):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-470, y=y_positions[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 427:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} is the winner!")
            else:
                print(f"You've lost! The {winning_color} is the winner!")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)
    



screen.exitonclick()