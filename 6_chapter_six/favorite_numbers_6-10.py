#Make dictionares about numbers.
favorite_numbers = {
        'phil': [3,7],
        'sara': [29,9],
        'ben': [10],
        'stev': [5,15,25],
        'john': [3],
        }

#Make loop to print message about favorite numbers.
for name, numbers in favorite_numbers.items():
    print("\nFavorite numbers " + name.title() + " is:")
    for number in numbers:
        print("\t- " + str(number))
