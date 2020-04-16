# HL components 5 - no duplicates

# To do
# set up empty list called already_guessed
# when user guesses, add guess to list
# for each guess, check that number is not in already_guessed

# HL components 5 - Prevents  duplicates guesses

SECRET = 7
GUESSES_ALLOWED = 4

already_guessed = []
guesses_left = GUESSES_ALLOWED
num_won = 0

guess = ""

while guess != SECRET and guesses_left >=1:

    guess = int(input("Guess: "))

    # check that guess is not a duplicate
    if guess in already_guessed:
        print("You already that number! Please try again. "
              "You *still* have {} guesses left".format(guesses_left))
        continue

    guesses_left -= 1
    already_guessed.append(guess)

    # If user has guesses left..
    if guesses_left >= 1:
        if guess > SECRET:
         print("Too high, try a lower number. Guesses Left: {}".format(guesses_left))
        elif guess < SECRET:
         print("Too low, try a higher number. Guesses Left: {}".format(guesses_left))

    # if the user is out of guesses
    else:
        # print ("Too high Or Too Low ")
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
        print("Congratulation ! you have guessed it right in {} guesses".format(len(already_guessed)))
        num_won += 1
#User has run out of guesses (and loses the game)
else:
    print("Sorry- You lose this round as you have run out of guesses")

