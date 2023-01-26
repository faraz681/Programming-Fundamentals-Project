import TicTacToe
import Hangman
import RockPaperScissors

# Main Menu of the Game


def DisplayMainMenu():
    print("1: TicTacToe \n2: Hangman \n3: Rock Paper Scissors \n")

# Once the game has been selected, this will display the mode selection menu


def DisplayGameMenu():
    print("1: P1 VS COMP \n2: P1 VS P2 \n")

# Input which game user wants to play
# Validate the input to only one character and only 1 2 or 3 as no other possible game


def OptionOne():
    option = input('Enter your corresponding key: \n')
    while option not in ('1', '2', '3'):
        option = input('Key not recognised, Please enter a valid key: \n')
    return option

# Input the mode where 1 indicates to play against computer and 2 to play multiplayer
# Validate the input as Option1


def OptionTwo():
    option = input('Enter your corresponding key: \n')
    while option not in ('1', '2'):
        option = input('Key not recognised, Please enter a valid key: \n')
    return option

# Ask if user wants to end game and Exit or keep playing
# Validate the input to only be either Y or N


def ContinueExit():
    option = input(
        'Would you like to continue playing? Press Y for yes N for no \n').upper()
    while option not in ('Y', 'N'):
        option = input(
            'Key not recognised, Please press valid key: \n').upper()
    return option


# The main functionality of entire game
if __name__ == '__main__':
    while True:
        DisplayMainMenu()
        option1 = OptionOne()
        DisplayGameMenu()
        option2 = OptionTwo()
        if option1 == '1':
            TicTacToe.TicTacToeMain(option2)
        elif option1 == '2':
            Hangman.HangmanMain(option2)
        else:
            RockPaperScissors.RockPaperScissorsMain(option2)
        user_input = ContinueExit()
        if user_input == 'N':
            print('Goodbye!')
            break
