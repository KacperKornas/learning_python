# Create, and open a file with append method.
filename = 'guest_book.txt'
name = ''

print("If you want to close program, write 'quit'.\n")
with open(filename, 'a') as file_object:
    # A loop that asks users for a name and adds it to 'quest_book.txt'.
    while name != 'quit':
        name = input("What is your name? ")
        if name != 'quit':
            print(f"Hello {name}!")
            print(f"Your name is now in guest book.\n")
            file_object.write(f"{name}\n")
    else:
        False
