usersLifeYears = int(input('How old are you? '))
usersRemainingLifeYears = 90 - usersLifeYears
usersRemainingLifeMonths = usersRemainingLifeYears * 12
usersRemainingLifeWeeks = usersRemainingLifeYears * 52
usersRemainingLifeDays = usersRemainingLifeYears * 365

print(f'You have about {usersRemainingLifeDays} Days, {usersRemainingLifeWeeks} weeks, {usersRemainingLifeMonths} months or {usersRemainingLifeYears} left.')