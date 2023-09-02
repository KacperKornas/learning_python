# Create function which prints the name of each magician in the list.
def show_magicians(magicians):
    """Print the name of each magician."""
    for magician in magicians:
        print(magician.title())

def make_great(magicians):
    """Modifies the list of magicians by adding the phrase 'the Great'."""

    # Build a new list to hold the great magicians.
    great_magicians = []

    # Make each magician great, and add it to great_magicians.
    while magicians:
        magician = magicians.pop()
        great_magician = (f"{magician.title()} the Great!")
        great_magicians.append(great_magician)

    # Add the great magician back into magician.
    for great_magician in great_magicians:
        magicians.append(great_magician)

# Make a list.
magicians = ['harry potter', 'ronald weasley', 'hermiona granger']

print("\nOrginal magicians:")
show_magicians(magicians)
make_great(magicians)

print("\nGreat magicians:")
show_magicians(magicians)