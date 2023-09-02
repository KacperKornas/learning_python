# Make a dictionary with a information about users.

lkosecka = {
        'first_name': 'lucja',
        'last_name': 'kosecka',
        'age': 23,
        'city': 'kraków'
        }
        
hkosecka = {
        'first_name': 'helena',
        'last_name': 'kosecka',
        'age': 19,
        'city': 'żegocina',
        }

akosecka = {
        'first_name': 'alicja',
        'last_name': 'kosecka',
        'age': 49,
        'city': 'żegocina',
        }
        
        
# Make a list with users.

people = [lkosecka, hkosecka, akosecka]
      
      
# Make a loop to print everything we know about this users.

for person in people:
    full_name = person['first_name'].title() + " " + person['last_name'].title()
    age = person['age']
    city = person['city']
    print(full_name.title() + ", of " + city.title() + ", is " + str(age) + " years old.")
    
    
