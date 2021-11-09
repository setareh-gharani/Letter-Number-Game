
import random 

#generate a numbergame

secret_number = random.randint (1, 10) 

def run_game():
    guesses = []
    guess=0

    while len( guesses ) < 5:
        #safly make an int
        try:
            guess=int(input("guess  number between 1 to 10:"))
        except ValueError :
            print("{} isn't a number".format(guess))
        else:
            if guess== secret_number:
                print("you got it my secret number {} ".format(secret_number))  
                break
            elif guess > secret_number:
                print("my number is lower than {}".format(guess))
            elif guess < secret_number:
                print("my number is higher than {}".format(guess))

            else:
                print("that's not it") 
        guesses.append(guess)        
    else:
        print("you didn't get it my number was {}".format(secret_number))  
    play_again=input("do you want play again? y/n")         
    if play_again.lower() !='n' :
        run_game()
    else:
        print("bye")

run_game()                     

