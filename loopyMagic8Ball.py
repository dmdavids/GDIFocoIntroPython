# Final Magic 8 Ball Program with A LOOP
# includes all 20 messages

# import the random module
import random

playAgain = "y"  # sentinel variable indicates if playing another game
while playAgain != "n":  # keep playing unless the user types 'n' for no

    # clear the screen by printing multiple lines
    print("\n"*15)

    # print out a welcome message to the user
    print("======= Welcome to the Magic 8 Ball Program =========")

    # ask the user for their question
    input("Please Enter Your Question for the Magic 8 Ball.\n")

    # this variable stores a triple-quoted string with an image of
    # the magic 8 ball to display before the message
    titleImage = """
                 ZZOOO88DDNNMM              
             7$7$$ZZZOO88DNNNMMMM+          
           Z7II777$$ZZO88DDNNMMMMMMM        
         ,77?::+77$$ZOOO8DDNNMMMMMMMM       
        $$$7I=+I77$$ZOO88DDNNMMMMMMMMMM     
       OZ$$777777$$ZZOO88DDNNMMMMMMMMMMM    
     .OOZZ$$$$$$$$ZMMMMONMMMMMMMMMMMMMMMM   
     N8OOZZZZZ$ZZMD         +MMMMMMMMMMMM$  
     D888OOOOOOOM             ZMMMMMMMMMMM  
    =DD8888O8OOM    I8DD888    $MMMMMMMMMM  
    NNNDDD8888M     N     D.    $MMMMMMMMMM 
    MNNNNNNDDDM     N    .D,    OMMMMMMMMMM 
    MMMMMNNNNNM     8MDDDDN.    ZMMMMMMMMMM 
    MMMMMMMMMMM     M     M,    +MMMMMMMMMM 
     MMMMMMMMMMD    M     M,   ,MMMMMMMMMM. 
     MMMMMMMMMMMZ   .~~~~~.   .MMMMMMMMMMM. 
     ZMMMMMMMMMMMO.          ~MMMMMMMMMMM.  
     .MMMMMMMMMMMMMD7~   ,=8MMMMMMMMMMMMM   
       MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM    
       .MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM     
          MMMMMMMMMMMMMMMMMMMMMMMMMMM       
           IMMMMMMMMMMMMMMMMMMMMMMM=        
              MMMMMMMMMMMMMMMMMMM           
                 MMMMMMMMMMMMM.                                                                                       
    """

    # generate a random number between 1 and 20
    # this is the message that will be printed
    answer = random.randint(1, 20)

    # check the answer value and then print a messsage
    # assigned to that value.  I randomly assigned the messages.
    # before I print the answer I print the image of the 8 ball 
    if answer == 1:
        print(titleImage)
        print("It is certain")
    elif answer == 2:
        print(titleImage)
        print("It is decidedly so")
    elif answer == 3:
        print(titleImage)
        print("Without a doubt")
    elif answer == 4:
        print(titleImage)
        print("Yes, definitely")
    elif answer == 5:
        print(titleImage)
        print("You may rely on it")
    elif answer == 6:
        print(titleImage)
        print("As I see it, yet")
    elif answer == 7:
        print(titleImage)
        print("Most likely")
    elif answer == 8:
        print(titleImage)
        print("Outlook good")
    elif answer == 9:
        print(titleImage)
        print("Yes")
    elif answer == 10:
        print(titleImage)
        print("Signs point to yes")
    elif answer == 11:
        print(titleImage)
        print("Reply hazy try again")
    elif answer == 12:
        print(titleImage)
        print("Ask again later")
    elif answer == 13:
        print(titleImage)
        print("Better not tell you now")
    elif answer == 14:
        print(titleImage)
        print("Cannot predict now")
    elif answer == 15:
        print(titleImage)
        print("Concentrate and ask again")
    elif answer == 16:
        print(titleImage)
        print("Don't count on it")
    elif answer == 17:
        print(titleImage)
        print("My reply is no")
    elif answer == 18:
        print(titleImage)
        print("My sources say no")
    elif answer == 19:
        print(titleImage)
        print("Outlook not so good")
    elif answer == 20:
        print(titleImage)
        print("Very doubtful")
    # just in case I have a bug I catch all other values here
    else:
        print("Oops! The Magic 8 Ball didn't work!")

    # Ask the user if they want to play again
    playAgain = input("Do you want to play again?")

# make sure that the user gets to see their message
input("\n\nPress Enter to Exit")
