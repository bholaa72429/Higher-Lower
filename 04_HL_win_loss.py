# To do
# Set up number of guesses
# Count # of guesses
# if user runs out of guesses, print 'you lose'
# if user guesses the secret number within the number of guesses print 'well done'

SECRET = 7
GUESSES_ALLOWED = 4

# initialise variables
guesses_left = GUESSES_ALLOWED
num_won = 0
guess = ""

# start game
while guess != SECRET and guesses_left >=1:

    guess = int(input("Guess: "))
    guesses_left -= 1

    # If user has guesses left..
    if guesses_left >= 1:
        if guess > SECRET:
         print("Too high, try a lower number")
        elif guess < SECRET:
         print("Too low, try a higher number")

    # if the user is out of guesses
    else:
        # print ("Too high Or Too Low  and sorry your out of guesses")
        if guess > SECRET:
         print("Too high !")
        elif guess < SECRET:
         print("Too low! ")
if guess == SECRET:
    # If user guessed right the first time...
    if guess == SECRET and guesses_left ==3:
        print("Amazing!  You got it in one guess")
    #If user has had more than one guess...
    else:
        print("Congratulation ! you have guessed it right!!")
#User has run out of guesses (and loses the game)
else:
    print("Sorry- You lose this round as you have run out of guesses")




            
