userYear = int(input('What year do you have a question about?\n'))

if userYear % 4 == 0:
    if userYear % 100 == 0:
        if userYear % 400 == 0:
            print(f'{userYear} is a leap year.')
        else:
            print(f'{userYear} is not a leap year.')
    else:
        print(f'{userYear} is a leap year.')
else:
    print(f'{userYear} is not a leap year.')