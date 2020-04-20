# Number checking function goes here
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

# Main routine

lowest = intcheck("Low Number: ")
highest = intcheck("High Number:", lowest + 1)
rounds = intcheck("Rounds ", 1)
guess = intcheck("Guess:" ,lowest, highest)


keep_going = ""
while keep_going == "":

    SECRET = 7
    GUESSES_ALLOWED = 4


    rounds = int(input("How many rounds? "))
    game_stats = []

    num_won = 0
    rounds_played = 0

    while rounds_played < rounds:
        guess = ""
        guesses_left = GUESSES_ALLOWED

        while guess != SECRET and guesses_left >=1:

            guess = int(input("Guess: "))
            guesses_left -= 1

            if guesses_left >= 1:

                if guess > SECRET:
                    print("Too high, try a lower number")

                elif guess < SECRET:
                    print("Too low, try a higher number")
            else:
                if guess > SECRET:
                    print("Too high !")
                elif guess < SECRET:
                    print("Too low ! ")

        if guess == SECRET:
            if guess == SECRET and guesses_left ==3:
                print("Amazing!  You got it in one guess")
            else:
                 print("Congratulation ! you have guessed it right in {} guesses".format(GUESSES_ALLOWED))
            num_won += 1
        else:
            print("Sorry- You lose this round as you have run out of guesses")
            guesses_left -= 1 # negative point for losing

        game_stats.append(GUESSES_ALLOWED - guesses_left)
        print("Won: {} \t \t Lost: {}".format(num_won, rounds_played - num_won + 1))
        rounds_played += 1
    # print each round outcome
    print()
    print("***Game Scores****")
    list_count = 1
    for item in game_stats:

        # indicates if game has ben won or lost
        if item > GUESSES_ALLOWED:
            status = "lost, run out of guesses"
        else:
            status = "won"
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

print("Thank you for playing. Good bye")


