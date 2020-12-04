def addingEven():
    maxRange = int(input('I will add all the even numbers to in your range.\nWhat is the max range you\'d like to add?'))
    totalSum = 0
    for i in range(0, maxRange, 2):
        totalSum += i
    print(totalSum)

addingEven()