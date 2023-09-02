learning_python = 'learning_python.txt'

with open(learning_python) as file_object:
    my_python = file_object.read()
print(my_python)
print('\n\n')


my_c = my_python
my_c = my_c.replace('Python','C')
print(my_c)