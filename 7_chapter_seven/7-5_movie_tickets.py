prompt = "\nEnter your age: " #defining information for people


while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print("Your ticket is free.")
    elif 3 <= age < 12:
        print("Your ticket cost $10.")
    elif age >= 12:
        print("Your ticket cost $15.")
