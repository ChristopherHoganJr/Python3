import math

wallHeight = int(input('What is the height of the wall?: '))
wallWidth = int(input('What is the width of the wall?: '))
paintCan = int(input('How many quarts do the paint cans hold?: '))

def paintNeeded(wallHeight, wallWidth, paintCan):
    area = wallHeight * wallWidth
    paintCansNeeded = math.ceil(area / paintCan)
    print(f'You will need {paintCansNeeded} cans of paint to finish this project')

paintNeeded(wallHeight, wallWidth, paintCan)