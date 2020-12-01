print('Welcome to the rollercoaster')
height = int(input('How tall are you in feet?\n'))
bill = 0

if height >= 5:
    print('You can ride this rollercoaster!')
    age = int(input('What is your age?\n'))
    if age < 12:
        print('Child tickets are $5')
        bill += 5
    elif age <= 18:
        print('Youth tickets are $7.')
        bill += 7
    elif age >= 45 and age <= 55:
        print('As a treat, you can ride for free today')
    else:
        print('Adult tickets are $12')
        bill += 12

    wantsPhotoInput = input('Do you want a photo taken? Y or N.\n')
    wantsPhoto = wantsPhotoInput.lower()
    if wantsPhoto == 'y':
        # Add $3 to bill
        bill += 3
    else:
        bill += 0

    print(f'Your total bill comes out to ${bill}.')
else:
    print('Sorry, you are not tall enough for this ride.')