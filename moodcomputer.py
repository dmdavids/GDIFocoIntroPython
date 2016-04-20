# Mood Computer
# Demonstrates the elif clause

#import random module
import random

# welcome screen
print("I sense your energy.  Your true emotions are coming across my screen.")
print("You are...")

#generate a random number between 1 and 3
mood = random.randint(1, 3)

#if mood is equal to 1, print a happy face
if mood == 1:
    # happy
    print( \
    """
       -----------
       |         |
       | O    O  |
       |   <     |
       |         |
       | .     . |
       |  `...`  |
       -----------
                   """)
# else if mood is equal to 2, print a neutral face
elif mood == 2:
    # neutral  
    print( \
    """
       -----------
       |         |
       | O    O  |
       |   <     |
       |         |
       | ------  |
       |         |
       -----------
                   """)
# else if mood is equal to 3 print a sad face
elif mood == 3:
    # sad
    print( \
    """
       -----------
       |         |
       | O    O  |
       |   <     |
       |         |
       |  .'.    |
       | '   '   |
       -----------
                   """)
# anything but 1, 2 or 3 and an error is reported, this should never happen
else:
    print("Illegal mood value!  (You must be in a really bad mood).")

# print end message
print("...today.")

# pause and wait for user input
input("\n\nPress the enter key to exit.")






