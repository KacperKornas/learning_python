cats = 'cats.txt'
dogs = 'dogs.txt'

# with open(cats, 'w') as f_obj:
#     f_obj.write("Stray\nTiger\nKulpetor")
#
# with open(dogs, 'w') as f_obj:
#     f_obj.write("Boris\nFluffy\nMax")

try:
    with open(cats) as  f_obj:
        cats_list = f_obj.read()
        print(cats_list)

except FileNotFoundError:
    pass

try:
    with open(dogs) as f_obj:
        dogs_list = f_obj.read()
        print(f"\n{dogs_list}")

except FileNotFoundError:
    pass
