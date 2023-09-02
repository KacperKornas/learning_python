with open('dracula.txt') as f_object:
    vampire = f_object.read()

print(vampire.count('night'))
print(vampire.count('the'))
