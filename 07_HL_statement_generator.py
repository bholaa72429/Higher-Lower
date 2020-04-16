# HL component 7 - Statement Generator

def h1_statement(statement, char):
    print()
    print(char*len(statement))
    print(statement)
    print(char*len(statement))
    print

# Main routine
too_low = h1_statement("^^ Too low, try a higher number.  |  "
                       "Guesses Left: 3 ^^", "^")
print()
too_high = h1_statement("vv Too high, try a lower number.  |   "
                         "Guesses Left: 2 vv", "v")
print()
duplicate = h1_statement(" !! You already guessed that # Please try again. |  "
                        "Guesses Lefts: 2 !!", "!" )
print()
well_done = h1_statement("*** Well done! You got it in 3 guesses ***", "*" )

print()
start_round = h1_statement("### Round 1 of 3 ###", "#")
