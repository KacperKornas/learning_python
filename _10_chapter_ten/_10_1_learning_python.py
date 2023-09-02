# Open file, take each line from file and stores it in a list.
with open('learning_python.txt') as file_object:
    my_experience_python = file_object.readlines()

# Create an empty string and loop which add each line from file to this string.
lines = ''
for line in my_experience_python:
    lines += line

print(lines)
print('\n\n')


# Add file to variable and open it.
experience_python = 'learning_python.txt'
with open(experience_python) as file_object:
    your_experience_python = file_object.read()

    print(your_experience_python)
print('\n\n')


# Add file to variable and open it.
more_experience_python = 'learning_python.txt'
with open(experience_python) as file_object:
    # Create a loop which print each line from file.
    for line in file_object:
        print(line.rstrip())