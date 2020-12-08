from yearDictionary import months

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    if month == '1' or month.lower() == 'january':
        month = months['January']
    elif month == '2' or month.lower() == 'february':
        month = months['February']
    elif month == '3' or month.lower() == 'march':
        month = months['March']
    elif month == '4' or month.lower() == 'april':
        month = months['April']
    elif month == '5' or month.lower() == 'may':
        month = months['May']
    elif month == '6' or month.lower() == 'june':
        month = months['June']
    elif month == '7' or month.lower() == 'july':
        month = months['July']
    elif month == '8' or month.lower() == 'august':
        month = months['August']
    elif month == '9' or month.lower() == 'september':
        month = months['September']
    elif month == '10' or month.lower() == 'october':
        month = months['October']
    elif month == '11' or month.lower() == 'november':
        month = months['November']
    elif month == '12' or month.lower() == 'december':
        month = months['December']
    else:
        return 'Invalid month'
    if is_leap(year) and month == months['February']:
        month.update({'Month Days': 29})
    return month['Month Days']

year = int(input('Enter a year: '))
month = input('Enter a month: ')
days = days_in_month(year, month)
print(f'There are {days} days in {month.title()}, {year}.')