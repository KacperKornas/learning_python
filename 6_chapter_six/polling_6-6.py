favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
 
people = ['phil', 'sarah', 'georg', 'ben', 'bonie']

for person in people:
    if  person in favorite_languages.keys():
        print(person.title() + " thank you for taken the poll.")
    else:
        print(person.title() + " please take the poll.")
