def bandNameGenerator():
    # Greeting
    print('Welcome to the Band Name Generator.')
    # Store the user's hometown
    cityName = input('What\'s the name of the city you grew up in?\n')
    # Store the user's pet name
    petName = input('What\'s the name of the last pet you had?\n')
    # Print the combination of strings and variables
    bandName = cityName + ' ' + petName
    print(f'Your band name is: {bandName}')
    again = input('Do you want to try again?\n')
    if again.lower() == 'yes':
        bandNameGenerator()
    else:
        print(f'Go show the world what {bandName} is made of!')

bandNameGenerator()