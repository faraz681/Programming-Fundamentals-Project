# Programming-Fundamentals-Project
Created basic command line games (Tic Tac Toe, Hangman and Rock Paper Scissors) for Programming Fundamentals Course Project. 

Each game has been defined as a separate function so that it is easier to combine them together
Each game will have 2 different modes to play:
1) P1 vs P2
2) P1 vs Computer
The code allows user to choose which game and mode they want to play

Proper validation checks are included where necessary:
After every complete game, ask the user if they want to continue playing or exit the game.

## Game-Wise Logic
### Tic Tac Toe

The basic board layout will be printed using arrays.

The code should check that the user doesn’t enter a pre occupied value and the
programm doesn’t overwrite the value. For example following the previous input P2
also decides to enter 2, the program should output a valid error message saying that the
location is already occupied.
The vs Computer will work the same way. random.randint() will be used to come up
with random numbers (between a specific and valid range). If the computer comes up
with a preoccupied index It should again output a valid error message as P1 already has
their symbol placed at that location.
Winning statements to be checked after every turn. If any of the conditions becomes true
the program halts. If no winning condition becomes true and maximum turns have been
reached the program halts saying its a tie.

### Rock Paper Scissors
Ask the user for input from 3 options, rock paper or scissor. Meanwhile the computer will
randomly select its option. Check for winning conditions and update the points. In case
of P1 VS P2, both players will be given an option to choose from 3 options. As soon as
P1 selects a valid corresponding number the screen is cleared to avoid P2 from

identifying P1’s choice. The validation process repeats for the choice entered by P2.
Once both inputs have been validated, they are compared in winning conditions
function. In case of both choices being same, the program outputs its a Draw!

### Hangman
P1 will enter a word. Based on the length of the word there will be blank spaces shown
up on the screen and a few characters being displayed. P2 will enter their guess letter, if
the letter was there in the word entered it will be shown up on the screen. The program
will halt if the number of turns exceeds the maximum limit or if P2 guesses the word
correctly. In the case of VS Computer, the computer randomly generates a word with the
help of the text file that contains all the dictionary words. Based on the length of the word
the screen displays randomly filled blanks. The program stops if user correctly guesses
the word or if they run out of tries.
