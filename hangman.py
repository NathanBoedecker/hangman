'''
Created on Feb 9, 2020

@author: ITAUser
'''

import random
from ctypes.wintypes import WORD

def pick_random_word():
    with open ("words.txt", 'r') as f: 
        words = f.readlines()
    index= random.randint(0,len(words)-1)
    
    word = words[index].strip()
    return word 

def ask_user_for_next_letter():
    letter = input("Guess your letter: ")
    return letter.strip().upper()
def generate_word_string(word, letters_guessed):
    
    
    output = []
    for letter in word:
        if letter in letters_guessed:
            output.append(letter.upper())
        else:
            output.append("_")  
  
    return " ".join(output)

    
if __name__ == '__main__' :
    WORD = pick_random_word()

    letters_to_guess = set(WORD)       
    correct_letters_guessed = set() 
    incorrect_letters_guessed = set()
    num_guesses = 0
    
    print("Welcome to Hangman!")
    
    #loop repeats the guessing sequences until user guesses all letters or runs out of guesses
    while((len(letters_to_guess) > 0) and num_guesses < 6):
        guess = ask_user_for_next_letter()
        guess = guess.lower()
        
    #check if user already guessed that letter
        if guess in correct_letters_guessed or \
            guess in incorrect_letters_guessed:
            print("You already guessed that letter.")
            continue
    #check if guess was correct
        if guess in letters_to_guess:
            letters_to_guess.remove(guess)
            correct_letters_guessed.add(guess)
        else:
            incorrect_letters_guessed.add(guess)
            num_guesses += 1
             
    #print how much of the word is guessed and how many letters are left
        word_string = generate_word_string(WORD, correct_letters_guessed)
        print(word_string)
        print("You have {} guesses left.".format(6 - num_guesses))
        
    #tell the user they have won or lost
    if num_guesses < 6:
        print("Congratulations! You correctly guessed the word {}")
    else:
        print("Sorry, you lose! Your word was {}" .format(WORD))
    
if num_guesses == 6:
    print("________   ")
    print("|      |   ")
    print("|      O   ")
    print("|     /|\  ")
    print("|     / \  ")
    print("|          ")
    print("|          ")
if num_guesses == 5:
    print("________   ")
    print("|      |   ")
    print("|      O   ")
    print("|     /|\  ")
    print("|     /    ")
    print("|          ")
    print("|          ")
if num_guesses == 4:
    print("________   ")
    print("|      |   ")
    print("|      O   ")
    print("|     /|\  ")
    print("|          ")
    print("|          ")
    print("|          ")
if num_guesses == 3:
    print("________   ")
    print("|      |   ")
    print("|      O   ")
    print("|     /|   ")
    print("|          ")
    print("|          ")
    print("|          ")
if num_guesses == 2:
    print("________   ")
    print("|      |   ")
    print("|      O   ")
    print("|      |   ")
    print("|          ")
    print("|          ")
    print("|          ")
if num_guesses == 1:
    print("________   ")
    print("|      |   ")
    print("|      O   ")
    print("|          ")
    print("|          ")
    print("|          ")
    print("|          ")
if(num_guesses == 0):
    print("________   ")
    print("|      |   ")
    print("|          ")
    print("|          ")
    print("|          ")
    print("|          ")
    print("|          ")
    
             

    