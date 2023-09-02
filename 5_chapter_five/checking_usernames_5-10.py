current_users = ['phil', 'ben', 'sara', 'JEREMI', 'BOB']
new_users = ['colin', 'sid', 'kevin', 'Jeremi', 'bob']

current_users_lower = [current_user.lower() for current_user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print("Sorry " + new_user + ", that name is taken.")
    else:
        print("Great, " + new_user + " is still available.")
