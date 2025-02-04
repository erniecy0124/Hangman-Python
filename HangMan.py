"A simple HangMan game that uses words from all the nouns in english language"

import random

FILENAME = '91K nouns.txt'

"""
Open the file based on the filename cand create a list of 
that contains all words.

PARAMETER:
filename: str
The filename.

RETURN:
words: list
A list filled with all of the words
"""
def open_file(filename : str) -> list:
    # Change this variable to access another text file
    file = open(filename, 'r')

    # Put the content in a list.
    words = file.read().splitlines()
    file.close()

    return words

"""
Select a random word and split the word into a list.

PARAMETER:
words: list
The list contains all the words retrieved from the file.

RETURN:
answer: list
A list contains the strings with the letters separated.
"""
def select_random_word(words: list) -> list:

    # Select a random word in the list of words and place it into a new list
    num_of_words = len(words)
    selected_num = random.randint(0, num_of_words - 1)
    selected_word = words[selected_num]
    selected_word = selected_word.lower()
    answer = list(selected_word)
    
    return answer

"""
Create a new list based on the selected word and replace it with '_'

PARAMETER:
selected_word: list
The selected_word in a list with its letters separated.

RETURN:
hidden_word: list
The word hidden by '_'
"""
def hide_word (selected_word: list) -> list:

    # Create a new list that will be filled with '_'
    hidden_word = ['_'] * len(selected_word)

    # Some noun contains symbol with '-' so we need to check and replace that area in the hidden list
    count = 0

    for x in selected_word:
        if x == '-':
            hidden_word[count] = '-'
        count += 1

    return hidden_word

"""
Welcome the user with the starting message.
"""
def welcome():
    print("Welcome to Python Hangman!")
    print("A random Noun will be selected as the Hidden Word!")
    print("You have 6 Chances to guess the correct letters in the word.")
    print("When you're ready, press 'enter'!\n")

"""
Function for when the user fails the first time
"""
def first_fail():
    print(" ----- ")
    print(" |   | ")
    print(" |   O ")
    print(" |     ")
    print(" |     ")
    print(" |     ")
    print("--------")

"""
Function for when the user fails the second time
"""
def second_fail():
    print(" ----- ")
    print(" |   | ")
    print(" |   O ")
    print(" |   | ")
    print(" |     ")
    print(" |     ")
    print("--------")

"""
Function for when the user fails the third time
"""
def third_fail():
    print(" ----- ")
    print(" |   | ")
    print(" |   O ")
    print(" |   |\\ ")
    print(" |     ")
    print(" |     ")
    print("--------")

"""
Function for when the user fails the fourth time
"""
def fourth_fail():
    print(" ----- ")
    print(" |   | ")
    print(" |   O ")
    print(" |  /|\\ ")
    print(" |     ")
    print(" |     ")
    print("--------")

"""
Function for when the user fails the fifth time
"""
def fifth_fail():
    print(" ----- ")
    print(" |   | ")
    print(" |   O ")
    print(" |  /|\\ ")
    print(" |  /  ")
    print(" |     ")
    print("--------")

"""
Function for when the user fails the sixth time
"""
def sixth_fail():
    print(" ----- ")
    print(" |   | ")
    print(" |   O ")
    print(" |  /|\\ ")
    print(" |  / \\ ")
    print(" |     ")
    print("--------")

"""
Display the current status of the Hangman based on how many times the user has failed.

PARAMETER:
fail_count: int
The number of times the user has failed.

"""
def display_fail(fail_count: int):

    if (fail_count == 1):
        first_fail()
    elif (fail_count == 2):
        second_fail()
    elif (fail_count == 3):
        third_fail()
    elif (fail_count == 4):
        fourth_fail()
    elif (fail_count == 5):
        fifth_fail()
    elif (fail_count == 6):
        sixth_fail()

"""
Check whether the user has inputted a valid letter

PARAMETER:
character: str
The letter the user has entered.

RETURN:
A boolean on whether the letter is valid.
"""
def letter_validity(character: str) -> bool:

    # Check if the character is an alphabet and that it doesn't exceed the length of 1
    if (character.isalpha() == False or len(character) > 1):
        return False
    return True

"""
Checked whether the letter the user inputted was already used.

PARAMETER:
character: str
The character the user entered.

user_letters: list
List of letters the user has already entered.

RETURN:
A boolean that indicate whether its true or false.
"""
def already_used_letters(character: str, used_letters: list) -> bool:

    for x in used_letters:
        if (x == character):
            return True
    return False

"""
Checked whether the letter the user inputted was already used.

PARAMETER:
character: str
The character the user entered.

user_letters: list
List of letters the user has already entered.

RETURN:
A boolean that indicate whether its true or false.
"""
def victory_validity(hidden_word: list) -> bool:

    for x in hidden_word:
        if (x == '_'):
            return False
    return True

def main():

    # Initialise variables
    words = open_file(FILENAME)
    word = select_random_word(words)
    correct_word = ''.join(word)
    hidden_word = hide_word(word)
    used_letters = []
    number_of_fails = 0
    number_of_correct_letters = 0

    for x in word:
        if (x != '-'):
            continue
        number_of_correct_letters += 1
    
    # Welcome the user
    welcome()

    while(True):
        user_input = input()
        if (user_input == ""):
            break
        else:
            print("Please enter a valid command.")
        
    print("The Hidden Word: " + str(hidden_word) + "\n")
    print("Used Letters: " + str(used_letters) + "\n")

    while(True):

        in_word = False
        user_letter = input("Please enter a guess: ")
    
        # Check if user's input is actually a letter.
        if (letter_validity(user_letter) == False):
            print("Please enter a letter.")
        
        elif (already_used_letters(user_letter, used_letters) == True):
            print("You have already used this letter, please enter another one!")
        else:
            index = 0
            # Go through and check if the user's guess is in the word
            for x in word:
                if (user_letter.lower() == x):
                    hidden_word[index] = user_letter
                    in_word = True
                index += 1
            used_letters.append(user_letter)
            
            if (in_word == False):
                number_of_fails += 1

                if (number_of_fails >= 6):
                    print("GAME OVER!! YOU HAVE LOST")
                    print("The word is " + str(correct_word) + "!")
                    break
            # Check if the user has won
            if (victory_validity(hidden_word) == True):
                print("Congragulations, you have Won!")
                print("The word is " + str(correct_word) + "!")
                break
        
        # Show the user the status of the hangman
        display_fail(number_of_fails)
        print("The Hidden Word: " + str(hidden_word) + "\n")
        print("Used Letters: " + str(used_letters) + "\n")

main()








        
        
       
        
            
     
            


        

    
        

    







    








