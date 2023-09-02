import json


def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def ask_correct_user():
    """Ask the user if this is a correct username."""
    with open('username.json') as f:

        name = json.load(f)
        print(f"{name.title()} is that you? ")
        answer = input("(yes/no) ")
        if answer == 'yes':
            print("Welcome back, " + name + "!")
        else:
            get_new_username()


def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")


ask_correct_user()
