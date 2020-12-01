print('Welcome to Python Pizza Deliveries')
total_cost = 0

# variables - Pizza Sizes
small_pizza = 15
medium_pizza = 20
large_pizza = 25


# Ask the size of the pizza
size = input('What size pizza do you want?\nsmall, medium, or large?\n')
size = size.lower()
if size == 'small' or size == 's':
    total_cost += small_pizza
    size = 'small'
if size == 'medium' or size == 'm':
    total_cost += medium_pizza
    size = 'medium'
if size == 'large' or size == 'l':
    total_cost += large_pizza
    size = 'large'

# What toppings does the user want
add_pepperoni = input('Do you want pepperoni?\n')
add_pepperoni = add_pepperoni.lower()
if add_pepperoni == 'yes' or add_pepperoni == 'y':
    if size == 'small':
        total_cost += 2
    else: 
        total_cost += 3
    add_pepporoni = True
else:
    add_pepperoni = False

extra_cheese = input('Do you want extra cheese?\n')
extra_cheese = extra_cheese.lower()
if extra_cheese == 'yes' or 'y':
    total_cost += 1
    extra_cheese = True
else:
    extra_cheese = False

# Give user the total price and reiterate the order. 
if add_pepperoni == False and extra_cheese == False:
    print(f'You ordered a {size} pizza. Your total bill is ${total_cost}.\n')
elif add_pepperoni == True and extra_cheese == False:
    print(f'You ordered a {size} pepperoni pizza. Your total bill is ${total_cost}.\n')
elif add_pepperoni == False and extra_cheese == True:
    print(f'You ordered a {size} pizza with extra cheese. Your total bill is ${total_cost}.\n')
else:
    print(f'You ordered a {size} pepperonia pizza with extra cheese. Your total bill is ${total_cost}\n')