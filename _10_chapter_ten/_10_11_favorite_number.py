import json


def ask_number():
    """Ask user about favorite number and save it in file."""
    number = input("What is your favorite number? ")
    with open('favorite_number.json', 'w') as f_obj:
        json.dump(number, f_obj)
        print("Thanks! I'll remember that.")


def show_number():
    """Print favorite number user."""
    with open('favorite_number.json') as f_obj:
        favorite_number = json.load(f_obj)
        print(f"I know your favorite number! It's {favorite_number}.")

ask_number()
show_number()