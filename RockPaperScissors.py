import os
import random

# Generate a random integer between 1-3 inclusive to choose from Rock Paper Scissor


def ComputerGenerate():
    comp = random.randint(1, 3)
    return comp

# Takes user input and validates it
# Must be a single numeric character
# In case above conditions don't meet, cintinously take input
# The clear() function helps to clear the user input value from terminal/CMD
# This prevents other player from reading what previous player had entered


def UserInput():
    user_input = input('Enter your corresponding choice: \n')
    while len(user_input) > 1 or user_input not in ('1', '2', '3'):
        user_input = input('Invalid key pressed, Please press a valid key: \n')
    if os.name == 'nt':
        def clear(): return os.system('cls')
    else:
        def clear(): return os.system('clear')
    clear()
    return int(user_input)

# Layout


def DisplayOptions():
    print('1: Rock \n2: Paper \n3: Scissors')

# checking every possible winning conditions


def CheckWinning(p1, p2):
    Win = False
    if (p1 == 1 and p2 == 3) or (p1 == 2 and p2 == 1) or (p1 == 3 and p2 == 2):
        Win = True
    return Win


def RockPaperScissorsMain(n):
    DisplayOptions()
    Optionlist = ['Rock', 'Paper', 'Scissors']
    print('Player1 Turn')
    Player1 = UserInput()  # Take Player1 input
    if n == '1':
        print('Computer Turn')  # Computer generate input
        Second = ComputerGenerate()
    else:
        DisplayOptions()
        print('Player2 Turn')  # Player 2 input
        Second = UserInput()
    Win = CheckWinning(Player1, Second)  # Checks for winning
    # Following lines helps identify who won and also outputs the corresponding choices
    # Of each player by tallying from the Optionlist
    if Win == True:
        print(
            f"Player1 wins! chose {Optionlist[Player1-1]} and opponent chose {Optionlist[Second-1]}")
    else:
        Win = CheckWinning(Second, Player1)
        if Win == True:
            print(
                f"Player2/Computer wins! chose {Optionlist[Second-1]} and opponent chose {Optionlist[Player1-1]}")
        else:
            print(f"Its a Draw! both chose {Optionlist[Second-1]}")
