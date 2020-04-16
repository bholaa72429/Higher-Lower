# HL component 10b - End Game States

# to do
# set up Games Play list with each rounds result
# set up average, best and worst score

SECRET = 7
GUESSES_ALLOWED = 4
rounds = int(input("How many rounds ? "))
game_stats = []

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

    game_stats.append(GUESSES_ALLOWED - guesses_left)
    print("Won: {} \t | \t Lost: {}".format(num_won, rounds_played - num_won + 1))
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

# Calculates statistics
game_stats.sort()
best = game_stats[0]
worst = game_stats[-1]
average = sum(game_stats)/len(game_stats)

print()
print("*** Summary Statistics ***")
print("Best: {}".format(best))
print("Worst: {}".format(worst))
print("Average: {:.2f}".format(average))


