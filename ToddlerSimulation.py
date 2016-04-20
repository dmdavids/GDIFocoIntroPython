# Three Year-Old Simulator
# Demonstrates the while loop

# print welcome screen
print("\tWelcome to the 'Three-Year-Old Simulator'\n")
print("This program simulates a conversation with a three-year-old child.")
print("Try to stop the madness.\n")

# 'prime' the loop by clearing out the value
# in the variable 'response'
response = ""

# while response is not equal to the word "Because."
# prompt the user for a new value for response
# response is the 'sentry variable'
while response != "Because.":
    response = input("Why?\n")

# Once the user has typed in "Because."
# this end message will print
print("Oh.  Okay.")

# Keep console open until user presses the enter key
input("\n\nPress the enter key to exit.")
