# HL component 9 - set up score mechanics

# To Do
# Set up round and win counter
# update feedback statement

SECRET = 7
GUESSES_ALLOWED = 4
rounds = 3

num_won = 0
rounds_played = 0

while rounds_played < rounds:
    guess = ""
    guesses_left = GUESSES_ALLOWED

    while guess != SECRET and guesses_left >=1:

        guess = int(input("Guess: "))
        guesses_left -= 1

    # If user has guesses left..
        if guesses_left >= 1:

           if guess > SECRET:
             print("Too high, try a lower number")

           elif guess < SECRET:
             print("Too low, try a higher number")
        else:
           if guess > SECRET:
            print("Too high !")

           elif guess < SECRET:
            print("Too low! ")

    if guess == SECRET:
        if guess == SECRET and guesses_left ==3:
         print("Amazing!  You got it in one guess")
        else:
         print("Congratulation ! you have guessed it right in {} guesses".format(GUESSES_ALLOWED))
        num_won += 1
    else:
        print("Sorry- You lose this round as you have run out of guesses")

    print("Won: {} \t \t Lost: {}".format(num_won, rounds_played - num_won + 1))
    rounds_played += 1

