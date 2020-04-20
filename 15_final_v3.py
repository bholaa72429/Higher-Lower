import random
import math
#function to print out messages with special character
def h1_statement(statement, char):
    print()
    print(char*len(statement))
    print(statement)
    print(char*len(statement))
    print

#integer checking function
def intcheck(question, low=None, high=None):
    # error messages
    if low is not None and high is not None:
            error = "Please enter an integer between {} and {}" \
            "(inclusive)".format(low, high)


    elif low is not None and high is None:
        error = "please enter an integer that is more than or " \
                "equal to {}".format(low)

    elif low is None and high is not None:
        error = "please enter an integer that is less than or "\
                "equal to {}".format(high)
    else:
        error = "Please enter an integer"

    while True:

        try:
            response = int(input(question))

            # check response is not too low
            if low is not None and response < low:
                print(error)
                continue

            # checks response is not too high
            if high is not None and response > high:
                 print(error)
                 continue

            return response

        except ValueError:
            print(error)
            continue

#Instruction

print("***Welcome to the Higher Lower Game***")
print()
print("To play...")
print()
print("-Enter the amount of rounds you would like to play.")
print("-Enter a low number.")
print("-Enter an high number.")
print("-Start guessing the secret number that is between your high and low number.")
print()
print("Now you can start playing. Good Luck!")

# Loop entire game ...
keep_going = ""
while keep_going == "":
    print()
    rounds = intcheck("How many Rounds you want to play? ", 1)
    print()
    game_stats = []
    num_won = 0
    rounds_played = 0

    while rounds_played < rounds:
        guess = ""

        lowest = intcheck("Enter a Low Number: ")
        highest = intcheck("Enter a High Number:", lowest + 1)
        range = highest - lowest +1
        max_raw = math.log2(range)
        max_upped = math.ceil(max_raw)
        GUESSES_ALLOWED = max_upped
        print("Maximum Guesses allowed: {}".format(GUESSES_ALLOWED))
        print()
        guesses_left = GUESSES_ALLOWED

        #creating a secret number between lowest and highest number entered
        SECRET = random.randint(lowest, highest)
        already_guessed = []
        while guess != SECRET and guesses_left >=1:
            guess = intcheck("Guess:" ,lowest, highest)
            guesses_left -= 1
            if guess in already_guessed:
                    h1_statement("^^ You already that number! Please try again.You still have {} guesses left ^^".format(guesses_left), "*")
            already_guessed.append(guess)

            if guesses_left >= 1:
                if guess > SECRET:
                    h1_statement("^^ Too High, try a lower number.  |  Guesses Left: {}^^".format(guesses_left), "^")

                elif guess < SECRET:
                    h1_statement("^^ Too Low, try a higher number.  |  Guesses Left: {}^^".format(guesses_left), "^")
            else:

                if guess > SECRET:
                    h1_statement("^^ Too HIGH !!!! ^^", "^")

                elif guess < SECRET:
                    h1_statement("^^ Too LOW !!!! ^^", "^")


        if guess == SECRET:
            if guess == SECRET and guesses_left == GUESSES_ALLOWED-1:
                h1_statement("***Amazing!  You got it in one guess***","*")
            else:
                 h1_statement("###Congratulation ! you have guessed it right in {} guesses###".format(GUESSES_ALLOWED-guesses_left),"#")
            num_won += 1
        else:
            print("Sorry- You lose this round as you have run out of guesses")
            guesses_left -= 1 # negative point for losing

        game_stats.append(GUESSES_ALLOWED - guesses_left)
        print("Won: {} \t \t Lost: {}".format(num_won, rounds_played - num_won + 1))
        rounds_played += 1
        print()
        print(" This is Round {}".format(rounds_played+1))
        print()
    # print each round outcome
    print()
    print("***Game Scores****")
    list_count = 1
    for item in game_stats:

        # indicates if game has ben won or lost
        if item > GUESSES_ALLOWED:
            status = "Lost, run out of guesses"
        else:
            status = "Won"
        print("Rounds {}: {} ({})".format(list_count, item, status))
        list_count += 1

    # Calculate (and then print) game statistics
    game_stats.sort()
    best = game_stats[0]
    worst = game_stats[-1]
    average = sum(game_stats)/len(game_stats)

    print()
    print("*** Summary Statistics ***")
    print("Best: {}".format(best))
    print("Worst: {}".format(worst))
    print("Average: {:.2f}".format(average))

    print()
    keep_going = input("Press <enter> to play again or any key to quit: ")
    print()
#farewell the user and end the game.
print("Thank you for playing. Good bye")
