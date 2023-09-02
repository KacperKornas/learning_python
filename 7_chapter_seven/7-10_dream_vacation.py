travels = {}
# active = True
while True:
    name = input("What is your name? ")
    travel = input("If you could visit one place in the world, where would you go? ")

    travels[name] = travel

    repeat = input("Would you like to let another person respond? (yes/ no)")
    if repeat == 'no':
        break
for name, travel in travels.items():
    print(f"{name} would like to go in {travel}.")


