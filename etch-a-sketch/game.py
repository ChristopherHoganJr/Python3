from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

# Can you either heading or left/right
def move_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def move_left():
    tim.left(10)
    tim.setheading(new_heading)

def move_backwards():
    tim.backwards(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

# add screen listener
screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()