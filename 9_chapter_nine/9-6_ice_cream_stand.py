class Restaurant():
    """A class representing a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = self.name + " serves wonderful " + self.cuisine_type + "."
        print("\n" + msg)

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = self.name + " is open. Come on in!"
        print("\n" + msg)

    def set_number_served(self, number_served):
        """Allow user to set the number of customers that have been served."""
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        """Allow user to increment the number of customers served."""
        self.number_served += additional_served

class IceCreamStand(Restaurant):
    """A class representing a ice cream stand."""

    def __init__(self, name, cuisine_type):
        """Initialize the ice cram stand"""
        super().__init__(name, cuisine_type)
        self.flavors = []

    def flavors_method(self):
        """Display flavors."""
        print("This flavors you can buy:")
        for flavor in self.flavors:
            print(f"-{flavor.title()}")

IceLand = IceCreamStand('IceLand', 'ice cream')
IceLand.flavors = ['bounty', 'cherry', 'green apple']

IceLand.flavors_method()