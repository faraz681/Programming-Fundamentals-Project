from pathlib import Path
import random
import os

# This function will generate a computer word by picking a random word from the
# text file 'dictionary_words.txt'
# random helps to come up with a random line number
# thus helps to fetch a random word from a randomly generated line number


def GenerateComputerWord():
    path = Path(__file__).parent / 'dictionary_words.txt'
    with path.open() as f:
        txt = f.read()
    word = txt.split()
    f.close()
    index = random.randint(0, len(word) - 1)
    comp_word = list(word[index].lower())
    return comp_word

# User will set the word in case of P1 Vs P2 has been selected
# The clear function will help clear the input by one player so other player can't identify what was typed
# the os.system('cls') acts for windows and 'clear' acts for linux/macos


def UserSetWord():
    user_Word = input('Enter your word:').lower()
    if os.name == 'nt':
        def clear(): return os.system('cls')
    else:
        def clear(): return os.system('clear')
    clear()
    user_Word = list(user_Word)
    return user_Word

# creates a blank list with _ corresponding to each character


def WordToBlank(word_list):
    blank_list = ['_' for i in range(len(word_list))]
    return blank_list

# randomly fills a few blanks
# index_generate generates number of blanks that must be visible based on the length of the word
# Then 'index _generate' amount of random indexes are generated and made sure they are not repeated
# These random index values are then replaced with orignal corresponding alphabets


def FillRandomBlanks(wl, bl):
    index_generate = int(len(bl) / 3)
    show_index = []
    for i in range(index_generate):
        random_index = random.randint(0, len(bl)-1)
        while random_index in show_index:
            random_index = random.randint(0, len(bl)-1)
        show_index.append(random_index)
    for i in show_index:
        bl[i] = wl[i]
    return bl

# Player gets 6 chances to guess the word
# If player guesses a letter which has already been entered, it doesn't count as a error
# If user guesses a single character more than once, the promp of already been guessed pops up
# Game ends when either the word has been guessed or errors exceed 6
# It is made sure that user only enters one alphabetical character at a time and no special or numeric character


def HangmanMain(choice):
    GuessedLetters = []
    if choice == '1':
        word = GenerateComputerWord()
    elif choice == '2':
        word = UserSetWord()
    Display_word = FillRandomBlanks(word, WordToBlank(word))
    Error = 6
    Found = False
    while Error != 0 and Display_word != word:
        print(f'You have {Error} attempts remaining to guess the word')
        print(' '.join(Display_word))
        user_input = input('Enter Your guess letter: \n').lower()
        while len(user_input) > 1 or ord(user_input) not in range(97, 123):
            user_input = input(
                'Inavlid character, please enter a valid alphabet: \n').lower()
        if user_input in GuessedLetters:
            print('You already guessed that letter, enter a different letter: \n')
            continue
        GuessedLetters.append(user_input)
        for i in range(len(word)):
            if word[i] == user_input:
                Display_word[i] = user_input
                Found = True
        if Found == False:
            Error -= 1
        Found = False
    if Error == 0:
        print(f"You ran out of tries, the correct word was {''.join(word)}")
    else:
        print(f"{''.join(word)} \nCongratulations, you guessed it right!")
