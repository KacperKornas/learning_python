filename = 'responses.txt'

print("If you want to close program, write 'quit'.\n")

# Create a loop that ask user to answer, and add opportunity to close.
while True:
    respond = input("Why do you like programming?\n")
    if respond == 'quit':
        break
    else:
        # Add respond to created file 'responses.txt'.
        with open(filename,'a') as file_object:
            file_object.write(f"{respond}\n")
        # Ask user whether it wants to continue.
        continue_poll = input("Would you like to respond again? (y/n)\n")
        if continue_poll != 'y':
            break
