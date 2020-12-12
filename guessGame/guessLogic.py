def setGameMode():
    print('+++ Select Game Mode +++')
    print('Easy mode will give you 10 chances and hard mode will give you 5.')
    gameMode = input('Which mode would you like to play?\n\'Easy\' or \'Hard\': ').lower()
    if gameMode == 'easy':
        return 'easy'
    elif gameMode == 'hard':
        return 'hard'
    else: 
        setGameMode()

def setGuesses(gameMode):
    if gameMode == 'easy':
        return 10
    elif gameMode == 'hard':
        return 5