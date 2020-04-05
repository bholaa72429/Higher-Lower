# HL component 3 - compares user guess with secret number

SECRET = 7

guess = ""

while guess != SECRET:

    guess = int(input("Guess:"))

    if guess > SECRET:
        print("Too high, try a lower number") # replace this with function call
    elif guess < SECRET:
        print("Too low, try a higher number")
    else:
        print("Well done! You guessed the secret number")
