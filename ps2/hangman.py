# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string
import sys

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    secret_word_array = list(secret_word)
    for letter in letters_guessed: 
        # continue_bool = True
        while letter in secret_word_array:
            secret_word_array.remove(letter)
    if len(secret_word_array) == 0:
        return True
    return False

# test case
# secret_word = 'mooi'
# letters_guessed = ['m', 'o', 'i']
# print(is_word_guessed(secret_word, letters_guessed))

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed_word_array = list()
    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word_array.append(letter)
        else: 
            guessed_word_array.append('_')
    return ''.join(guessed_word_array)

# test case
# print(get_guessed_word('mooi', ['m','i']))

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    available_letters = list(string.ascii_lowercase)
    for letter in letters_guessed:
        available_letters.remove(letter)
    return ''.join(available_letters)

# test case
# print(get_available_letters(['m','o','i']))

def validate_user_input(input, letters_guessed): 
    letters = list(string.ascii_letters)
    '''
    input: the input that the user has entered 
    checks if the input is a letter 
    returns: True or False
    '''
    if not input in letters:
        return 'Oops! That is not a valid letter.'
    if input in letters_guessed:
        return 'Oops! You\'ve already guessed that letter.'
    return 'all_good'

def get_unique_characters_in_string(string):
    '''
    string: string, the secret word
    gets unique characters
    returns the count of unique characters
    '''
    s = set(string) 
    return len(s)

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    print('Welcome to the game Hangman!')
    print(f'I am thinking of a word that is {len(secret_word)} letters long.\nYou have 3 warnings left.\n-------------')
    guesses_left = 6
    warnings = 3 
    letters_guessed = list()
    while guesses_left > 0: 
        print(f'You have {guesses_left} guesses left.')
        print(f'Available letters: {get_available_letters(letters_guessed)}')
        guessed_letter = input('Please guess a letter: ')
        validation = validate_user_input(guessed_letter, letters_guessed)
        if validation != 'all_good': 
            if warnings < 1: 
                guesses_left -= 1
            if warnings > 0: 
                warnings -= 1 
            print(f'{validation} You have {warnings} warnings left: {get_guessed_word(secret_word, letters_guessed)}\n-------------')
            continue
        guessed_letter = guessed_letter.lower()
        letters_guessed.append(guessed_letter)
        if guessed_letter in secret_word:
            print(f'Good Guess: {get_guessed_word(secret_word, letters_guessed)}\n-------------')
        else: 
            print(f'Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}\n-------------') 
            if guessed_letter in ['a', 'e', 'i', 'o', 'u']: 
                guesses_left -= 2
            else: 
                guesses_left -= 1
        if '_' not in get_guessed_word(secret_word, letters_guessed):
            score = get_unique_characters_in_string(secret_word) * guesses_left
            print(f'Congratulations, you won!\nYour total score for this game is: {score}')
            sys.exit(0)
    print(f'Sorry, you ran out of guesses. The word was {secret_word}')




# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    if len(my_word) != len(other_word):
        return False
    for i in range(len(my_word)): 
        if my_word[i] == '_':
          if other_word[i] in my_word: 
            return False 
          else: 
            continue
        if my_word[i] != other_word[i]: 
            return False
    return True

# test cases
# print(match_with_gaps("te_t", "tact"))
# #False
# print(match_with_gaps("a__le", "banana"))
# #False
# print(match_with_gaps("a__le", "apple"))
# #True
# print(match_with_gaps("a_ple", "apple"))
# #False

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    possible_matches = list()
    for word in wordlist: 
        if match_with_gaps(my_word, word):
            possible_matches.append(word)
    if len(possible_matches) == 0:
        return 'No matches found'
    return " ".join(possible_matches)

# # test cases
# print(show_possible_matches("t__t"))
# #tact tart taut teat tent test text that tilt tint toot tort tout trot tuft twit
# print(show_possible_matches("abbbb_"))
# #No matches found
# print(show_possible_matches("a_pl_"))
# #ample amply



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''

    print('Welcome to the game Hangman!')
    print(f'I am thinking of a word that is {len(secret_word)} letters long.\nYou have 3 warnings left.\n-------------')
    guesses_left = 6
    warnings = 3 
    letters_guessed = list()
    while guesses_left > 0: 
        print(f'You have {guesses_left} guesses left.')
        print(f'Available letters: {get_available_letters(letters_guessed)}')
        guessed_letter = input('Please guess a letter: ')
        if guessed_letter == '*':
            my_word = get_guessed_word(secret_word, letters_guessed)
            print(f'Possible word matches are:\n{show_possible_matches(my_word)}\n-------------')
            continue
        validation = validate_user_input(guessed_letter, letters_guessed)
        if validation != 'all_good': 
            if warnings < 1: 
                guesses_left -= 1
            if warnings > 0: 
                warnings -= 1 
            print(f'{validation} You have {warnings} warnings left: {get_guessed_word(secret_word, letters_guessed)}\n-------------')
            continue
        guessed_letter = guessed_letter.lower()
        letters_guessed.append(guessed_letter)
        if guessed_letter in secret_word:
            print(f'Good Guess: {get_guessed_word(secret_word, letters_guessed)}\n-------------')
        else: 
            print(f'Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}\n-------------') 
            if guessed_letter in ['a', 'e', 'i', 'o', 'u']: 
                guesses_left -= 2
            else: 
                guesses_left -= 1
        if '_' not in get_guessed_word(secret_word, letters_guessed):
            score = get_unique_characters_in_string(secret_word) * guesses_left
            print(f'Congratulations, you won!\nYour total score for this game is: {score}')
            sys.exit(0)
    print(f'Sorry, you ran out of guesses. The word was {secret_word}')


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
