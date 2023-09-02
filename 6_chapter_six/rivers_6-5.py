rivers = {
    'loara': 'france',
    'ren': 'germany',
    'severn': 'great britain'
    }
    
for river_name, country in rivers.items():
    print("The " + river_name.title() + " runs through " + country.title() + ".")
    
print("\nRiver name:")
     
for river_name in rivers.keys():
    print(" - " + river_name.title())

print("\nCountry:")

for country in rivers.values():
    print(" - " + country.title())
