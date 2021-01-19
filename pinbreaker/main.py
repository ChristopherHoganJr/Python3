import random

def PrintIntroduction(Difficulty):
    # Print welcome messages to the terminal
    print(f"\nAgent 6, we need your hacking skills to break the level {Difficulty} secrutiy pin")
    print("Enter the pin so we can get through this door\n\n")

def PlayGame(Difficulty):
    PrintIntroduction(Difficulty)
    nextLevel = False

    # Delcare 3 number variables
    CodeA = random.randint(1, 100) % Difficulty + Difficulty
    CodeB = random.randint(1, 100) % Difficulty + Difficulty
    CodeC = random.randint(1, 100) % Difficulty + Difficulty

    CodeSum = CodeA + CodeB + CodeC
    CodeProduct = CodeA * CodeB * CodeC

    while nextLevel == False:
        # Print sum and product to the terminal
        print("+ There are 3 digits in the pin")
        print(f"+ The digits add up to : {CodeSum}")
        print(f"+ The digits product is: {CodeProduct}\n")

        # Store player guesses
        UserPin = input("What is the pin number?: ")
        GuessA, GuessB, GuessC = map(int, UserPin.split())

        GuessSum = GuessA + GuessB + GuessC
        GuessProduct = GuessA * GuessB * GuessC

        if (GuessSum == CodeSum and GuessProduct == CodeProduct):
            print("Good work Agent 6. Let's move on.")
            break
        else:
            print("\nBe careful Agent 6. Try again\n")
    return True

LevelDifficulty = 1
MaxDifficulty = 5

while (LevelDifficulty <= MaxDifficulty):
    LevelComplete = PlayGame(LevelDifficulty)
    print(LevelComplete)
    if (LevelComplete == True):
        LevelDifficulty += 1

print("Great work Agent 6. You gained access and were undetected. Gather the intel and get out of there.")