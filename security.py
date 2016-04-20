# Granted or Denied
# Demonstrates an else clause

#Print splash screen advertisement
print("Welcome to Insecure Security Inc.")
print("-- where we're not good at security at all\n")

#input the password from the user
password = input("Enter your password: ")

# if the value the user typed in matches "secret"
# print "Access Granted"
if password == "secret":
    print("Access Granted")
#Otherwise, print "Access Denied"
else:
    print("Access Denied")

# Pause and wait for user to press enter key
input("\n\nPress the enter key to exit.")
