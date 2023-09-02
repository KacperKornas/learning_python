usernames = []

if usernames:

    for usernames in usernames:
        if usernames == 'admin':
            print("Hello " + usernames + ", would you like to see a status report?")
        else:
            print("Hello " + usernames + ", thank you for logging in again.")
else:
    print("We need to find some users!")

