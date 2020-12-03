import random

letters = ['a','A','b','B','c','C','d','D','e','E','f','F','g','G','h','H','i','I','j','J','k','K','l','L','m','M','n','N','o','O','p','P','q','Q','r','R','s','S','t','T','u','U','v','V','w','W','x','X','y','Y','z','Z']
number = ['0','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']

print('Welcome to the PyPassword Generator!')
nr_letters = int(input('How many letters would you like in your password?\n'))
nr_symbols = int(input('How many symbols would you like?\n'))
nr_numbers = int(input('How many numbers would you like?\n'))

# The list for the random characters
user_pw = []
# Iterate over the variable lists and add random variables to user_pw
for i in range(nr_letters):
    user_pw.append(letters[random.randint(0, len(letters)-1)])
for i in range(nr_numbers):
    user_pw.append(number[random.randint(0, len(number)-1)])
for i in range(nr_symbols):
    user_pw.append(symbols[random.randint(0, len(symbols)-1)])
# Shuffle the list items
random.shuffle(user_pw)
# Empty string to add list items to
password = ''
# Iterate over list items and add them to a string.
for i in user_pw:
    password += i
# Print the user's password
print(f'Your password is: {password}')