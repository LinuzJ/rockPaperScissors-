import random

def play():
    computer = random.choice(['r', 'p', 's'])
    user = getUserInput()

    if isWon(user, computer):
        return "The player won"
    elif user == computer:
        return "The game is a tie"
    else:
        return "The computer won"

def getUserInput():
    
    userinput = input('"r" for rock, "p" for paper, "s" for scissors\n')
    
    if userinput != "r" and userinput != 's' and userinput != 'p':
        print('Incorrect input, please try again!')
        userinput = input('"r" for rock, "p" for paper, "s" for scissors\n')

    return userinput


def isWon(player, opponent):
    if (player == "r" and opponent == "s") or (player == "p" and opponent == "r") or (player == "s" and opponent == "p"):
        return True
    else:
        return False

def game():
    counter = 0
    playerScore = 0
    computerScore = 0

    while counter < 5:
        storage = play()
        
        if storage == "The player won":
            playerScore += 1
        elif storage == "The computer won":
            computerScore += 1
        
        print(storage)
        print("The score is: " + str(playerScore) + "-" + str(computerScore))
        counter += 1


game()
        