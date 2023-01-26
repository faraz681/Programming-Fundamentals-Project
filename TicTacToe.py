import random
# Computer generates a random integer between 1-9 inclusive.
# The arr passed in the function is a list of preoccupied indexes.
# In case the generated number already exists in arr, the computer will generate a new number.


def CompTurn(arr):
    Computer_Input = random.randint(1, 9)
    while Computer_Input in arr:
        Computer_Input = random.randint(1, 9)
    return Computer_Input

# Function Player1() is used to take input from player 1 and validate it
# The input must be a single numeric character


def Player1():
    User_Input = input('P1 Enter the corresponding key: \n')
    while len(User_Input) > 1 or User_Input not in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
        User_Input = input(
            'Invalid Key, Please press the valid corresponding key: \n')
    return int(User_Input)

# Similar as Player1() function.


def Player2():
    User_Input = input('P2 Enter the corresponding key: \n')
    while len(User_Input) > 1 or User_Input not in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
        User_Input = input(
            'Invalid Key, Please press the valid corresponding key: \n')
    return int(User_Input)

# A board layout function.
# The base parameter is initially the list of numbers representing placement values.


def DisplayBoard(base):
    print('  |   |  ')
    print(base[0], '|', base[1], '|', base[2])
    print('---------')
    print('  |   |  ')
    print(base[3], '|', base[4], '|', base[5])
    print('---------')
    print('  |   |  ')
    print(base[6], '|', base[7], '|', base[8])
    print()

# Check for every possible winning condition.
# Diagonal,Horizontal,Vertical
# In case any of them turns out to be true, the Win return if True will indicate either player has won


def CheckWinning(base):
    Win = False
    if base[0] == base[1] == base[2] or base[0] == base[3] == base[6] or base[0] == base[4] == base[8]:
        Win = True
    elif base[1] == base[4] == base[7] or base[3] == base[4] == base[5]:
        Win = True
    elif base[2] == base[4] == base[6] or base[2] == base[5] == base[8]:
        Win = True
    elif base[6] == base[7] == base[8]:
        Win = True
    return Win

# The main tic tac toe game function.
# Initialise the Base List of initial values that each represent a corresponding placement value
# Turn variable acts as a counter to control the number of times the loop runs, in case of 9 it terminates


def TicTacToeMain(n):
    Base = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    DisplayBoard(Base)
    Turn = 0
    OccupiedIndex = []
    Symbol1 = 'X'
    Symbol2 = 'O'
    Win = False
    while Turn != 9 and Win != True:
        PlayerOneTurn = Player1()
        while PlayerOneTurn in OccupiedIndex:  # Checking if the user entered place value is preoccupied or not
            # In case of preoccupied, it asks for another unique value
            print('Place already occupied!')
            PlayerOneTurn = Player1()
        # Appending list of occupied indexes
        OccupiedIndex.append(PlayerOneTurn)
        # PlayerOneTurn - 1 acts as an index of list
        Base[PlayerOneTurn - 1] = Symbol2
        Turn += 1
        Win = CheckWinning(Base)  # Check Win Conditions
        DisplayBoard(Base)
        if Win == True or Turn == 9:  # Break the loop if win is true or turns has reached 9
            break
        if n == '1':
            # Repeat the same process as player 1 but this time for computer
            Place = CompTurn(OccupiedIndex)
            OccupiedIndex.append(Place)
            Base[Place-1] = Symbol1
            Turn += 1
            Win = CheckWinning(Base)
            DisplayBoard(Base)
        else:
            Place = Player2()  # For player 2
            while Place in OccupiedIndex:
                print('Place already occupied!')
                Place = Player2()
            OccupiedIndex.append(Place)
            Base[Place-1] = Symbol1
            Turn += 1
            Win = CheckWinning(Base)
            DisplayBoard(Base)
    if Win == True:
        if Turn % 2 != 0:  # In case Win == true and Turn value was odd, it indicates player 1 has won
            print('Congratulations Player1 Wins!')
        else:  # Since Win is True and turn is not odd, it means the other opponent has won
            if n == 1:
                print('Computer Wins the game!')
            else:
                print('Congratulations Player2 Wins1')
    else:  # No win and Turns being 9 indicates a Draw.
        print('Its a Draw!')
