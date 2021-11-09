
import random 
import os
import sys

# make a list of word 
words =['apple' , 'bennana', 'setareh', 'siavash' , 'eagle']


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')    



def draw( bad_gusses , good_guesses , secret_word):
    clear()
    print('strikes: {} /7'.format(len(bad_guesses)))
    print('')
    

    for letter in bad_guesses:
        print( letter , end= '')
    print('\n\n')    

    for letter in secret_word:
            if letter in good_guesses:
                print(letter , end= ' ')
            else:
                print('_' , end= ' ')
         
            print('_' , end='')     




def get_guess( bad_guesses , good_guesses , secret_word):
    while True:
        guess=input("Guess a letter : ").lower()

        if len (guess) != 1:
            print("you can only guess single letter :" )
            continue
        elif guess in bad_guesses or guess in good_guesses:
            print("you've alredy guess the letter")    
            continue
        elif not guess.isalpha():
            print("you can only guess letter")
        else:
            return guess    


def play(done):
    clear()
    secret_word = random.choice(words)
    bad_guesses=[]
    good_guesses=[]
  
    while True:
        draw( bad_guesses , good_guesses , secret_word)
        guess = get_guess(bad_guesses , good_guesses , secret_word)

        if guess in secret_word:
            good_guesses.append(guess)

        found = True
        for letter in secret_word:
            if letter not in good_guesses :
                found = False
            if found:
                print("you win")
                print("my secret word was {}".format(secret_word))
        else:
            bad_guesses.append(guess)        
            if len(bad_guesses) == 7 :
                draw(bad_guesses , good_guesses , secret_word)
                print("you lost")
                print("my secret word was {}".format(secret_word))
                done=True
        if done: 
            play_again= input('play again? Y/n '). lower()

            if play_again != 'n':
                return play(done = False)     
            else:
                sys.exit()    





while True:
    start = input (" press enter/return to start or enter Q to quit.")  


    if start.lower() == 'q':
        break

     # pick a random word
    
    secret_word = random.choice(words)

    bad_guesses=[]
    good_guesses=[]
    
    while len( bad_guesses) < 7 and len( good_guesses)  != len(list(secret_word)) :
        
       
        if guess in secret_word:
            good_guesses.append(guess)

            if len(good_guesses) == len(list(secret_word)):
                print("you win my secret word {}".format(secret_word))
                break

        else:
            bad_guesses.append(guess)

    else:
        print("you didn't guess secret word  mysecret word was {}".format(secret_word))

    
        



        









 


# draw spaces for letterguessing 
# take a guess
# draw guess letters and strikes
# print out win/lose