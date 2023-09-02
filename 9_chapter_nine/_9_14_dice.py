from random import randint

class Die:
    """A class to dice draw."""
    def __init__(self, sides):
        """Initialize dice."""
        self.sides = sides

    def roll_die(self):
        """Prints a random number between 1 and the number of sides."""
        number_sides = randint(1, self.sides)
        print(number_sides)

six_sided_die = Die(6)
six_sided_die.roll_die()
six_sided_die.roll_die()
six_sided_die.roll_die()
six_sided_die.roll_die()
six_sided_die.roll_die()
six_sided_die.roll_die()
six_sided_die.roll_die()
six_sided_die.roll_die()
six_sided_die.roll_die()
six_sided_die.roll_die()
six_sided_die.roll_die()

print("\n")
ten_sided_die = Die(10)
ten_sided_die.roll_die()
ten_sided_die.roll_die()
ten_sided_die.roll_die()
ten_sided_die.roll_die()
ten_sided_die.roll_die()
ten_sided_die.roll_die()
ten_sided_die.roll_die()
ten_sided_die.roll_die()
ten_sided_die.roll_die()
ten_sided_die.roll_die()
ten_sided_die.roll_die()

print("\n")
twenty_sided_die = Die(20)
twenty_sided_die.roll_die()
twenty_sided_die.roll_die()
twenty_sided_die.roll_die()
twenty_sided_die.roll_die()
twenty_sided_die.roll_die()
twenty_sided_die.roll_die()
twenty_sided_die.roll_die()
twenty_sided_die.roll_die()
twenty_sided_die.roll_die()
twenty_sided_die.roll_die()