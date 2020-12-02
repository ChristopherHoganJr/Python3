import random
# Ask who is going to eat the pizza?
names_string = input('Who is going to eat the pizza?\n ')
# Split the string and put he names in a list
names = names_string.split(', ')
# Figure out the size of the random numbers
randomName = random.randint(0, len(names)-1)
# Pick who will buy pizza
print(f'{names[randomName]} is going to buy the meal today.')
