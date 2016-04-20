# Final Magic 8 Ball Program with A LOOP
# includes all 20 messages

# import the random module
import random

playAgain = "y"  # sentinel variable indicates if playing another game
while playAgain != "n":  # keep playing unless the user types 'n' for no

    # YOUR ORIGINAL MAGIC 8 BALL GAME GOES HERE
    # NOTICE HOW THIS IS BLOCK INDENTED!

    # Ask the user if they want to play again
    playAgain = input("Do you want to play again?")

# make sure that the user gets to see their message
input("\n\nPress Enter to Exit")
