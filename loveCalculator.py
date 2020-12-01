print('Welcome to the Love Calculator!')
name1 = input('What is your name? \n')
name2 = input('What is their name? \n')

lowerName1 = name1.lower().strip()
lowerName2 = name2.lower().strip()

true = 'true'
love = 'love'
trueScore = 0
loveScore = 0


for i in range(len(name1)):
    for j in range(len(true)):
        if lowerName1[i] == true[j]:
            trueScore += 1
    for j in range(len(love)):
        if lowerName1[i] == love[j]:
            loveScore += 1       
for i in range(len(name2)):
    for j in range(len(true)):
        if lowerName2[i] == true[j]:
            trueScore += 1
    for j in range(len(love)):
        if lowerName2[i] == love[j]:
            loveScore += 1

totalScore = int(str(trueScore) + str(loveScore))

if totalScore < 10 or totalScore > 90:
    print(f'Your score is {totalScore}, you go together like coke and mentos.')
elif totalScore >= 40 and totalScore <= 50:
    print(f'Your score is {totalScore}, you are alright together.')
else:
    print(f'Your score is {totalScore}. Boring')