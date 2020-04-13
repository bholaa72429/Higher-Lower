# HL components 5 - no duplicates

# To do
# set up empty list called already_guessed
# when user guesses, add guess to list
# for each guess, check that number is not in already_guessed

# HL components 5 - Prevents  duplicates guesses

SECRET = 7
GUESSES_ALLOWED = 5

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
