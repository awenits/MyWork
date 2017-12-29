import random
import string

WORDLIST_FILENAME = "words.txt"
print("                                                                            ")
print("                                                                            ")
print(" H     H       A       N      N  GGGGGGGG  M       M       A       N      N ")
print(" H     H     A   A     N N    N  G         M M   M M     A   A     N N    N ")
print(" HHHHHHH    A A A A    N  N   N  G   GGGG  M   M   M    A A A A    N  N   N ")
print(" H     H   A       A   N    N N  G   G  G  M       M   A       A   N    N N ")
print(" H     H  A         A  N      N  GGGGG  G  M       M  A         A  N      N ")
print("                                                                            ")
print("                                 ,________     ")
print("                                 |       |     ")
print('                                 |      (")  save me !    ')
print("                                 |       I     ")
print("                                 |      /|\    ")
print("                                 |     / | \   ")
print("                                 |       |     ")
print("                                 |      / \    ")
print("                                 |     /   \   ")
print("                                /|\            ")
print("                               / | \           ")
print("                              #################")

#loading wordlist
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    #print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    #print("  ", len(wordlist), "words loaded.")
    return wordlist

#choosing random word
def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

#words list
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in secretWord:
        if not letter in lettersGuessed:
            return False
    return True

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessed_word = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            guessed_word += letter
        else:
            guessed_word += '_ '
    
    return guessed_word
    
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    available_letters = ''
    for letter in string.ascii_lowercase:
        if not letter in lettersGuessed:    
            available_letters += letter
    
    return available_letters
    
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.
    Starts up an interactive game of Hangman.
    * At the start of the game, let the user know how many 
      letters the secretWord contains.
    * Ask the user to supply one guess (i.e. letter) per round.
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.
    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.
    '''
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is", len(secretWord), "letters long.")
    count = 8
    lettersGuessed = []
    while(True):
        print("------------")
        #checking win or lose
        if getGuessedWord(secretWord, lettersGuessed) == secretWord:
            print("Congratulations, you won!")
            break
        if count == 0:
            print("Sorry, you ran out of guesses. The word was", secretWord + ".")
            break
        
        #for showing guesses available    
        print("You have", count, "guesses left.")
        
        #for avilable letters
        print("Available letters: ", getAvailableLetters(lettersGuessed))
        
        #get users input
        guess = input("Please guess a letter: ").lower()
        
        #store it in the list
        if not guess in lettersGuessed:
            lettersGuessed.append(guess)
            #intermediate steps
            if guess in secretWord:
                #if guess is right
                print("Good guess:",getGuessedWord(secretWord, lettersGuessed))
            else:
                #if guess is not right
                print("Oops! That letter is not in my word:",getGuessedWord(secretWord, lettersGuessed))
                #reduce no. of guess by 1
                count -= 1
        else:
            print("Oops! You've already guessed that letter:",getGuessedWord(secretWord, lettersGuessed))
        
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
