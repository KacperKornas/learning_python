favorite_places = {
    'lucja': ['gallery', 'club', 'gym'],
    'kacper': ['court', 'home', 'work'],
    'maksymilian': ['field', 'playground', 'cinema'],
    }

for name, places in favorite_places.items():
    print("\nFavorite places " + name.title() + " is:")
    for place in places:
        print("- " + place.title())
