# Make an empty list to store the pets in.
pets = []

#Make a several dictionares about pets.
pet = {
    'type': 'dog',
    'name': 'ami',
    'owner': 'lucja',
    }
    
pets.append(pet)

pet =  {
    'type': 'dog',
    'name': 'puszek',
    'owner': 'anita',
    }

pets.append(pet)

pet =  {
    'type': 'cat',
    'name': 'kulpetor',
    'owner': 'kacper',
    }

pets.append(pet)

pet =  {
    'type': 'turtle',
    'name': 'bob',
    'owner': 'bogdan',
    }

pets.append(pet)

pet =  {
    'type': 'parrot',
    'name': 'pepper',
    'owner': 'patrycja',
    }

pets.append(pet)


for pet in pets:
    print("\nHere's what I know about " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + value)
