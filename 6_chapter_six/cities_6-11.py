cities = {
    'kraków': {
        'country': 'poland',
        'population': 800000,
        'fact': 'I live here.'
            },
            
    'new york': {
        'country': 'USA',
        'population': 8400000,
        'fact': 'This city newer sleep.'
            },
            
    'berlin': { 
        'country': 'german',
        'population': 3600000,
        'fact': 'This city has pandas.'
            },
        }

for city, facts in cities.items():
    print("\nCity: " + city.title())
    print("Country: " + facts['country'].title())
    print("Population: " + str(facts['population']))
    print("Fact: " + facts['fact'])
    

    
