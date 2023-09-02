# Create function which prints the name of each magician in the list.
def show_magicians(magicians):
    """Print the name of each magician."""
    for magician in magicians:
        print(f"{magician.title()}")

# Make a list.
magicians = ['harry potter', 'ronald weasley', 'hermiona granger']
show_magicians(magicians)