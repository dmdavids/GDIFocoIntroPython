# Craps Roller
# Demonstrates random number generation

#import the random module
import random

# generate random numbers 1 - 6
die1 = random.randint(1, 6) #Generates a number between 1 and 6 
die2 = random.randrange(6) + 1 # Generates a number between 0 and 5
                               # then adds 1

# add the value of the two dice together
total = die1 + die2

# output result to the playerr
print("You rolled a", die1, "and a", die2, "for a total of", total)

# pause for player input before exiting console window
input("\n\nPress the enter key to exit.")
