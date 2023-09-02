class Restaurant():
    """A class representing a restaurant."""

    def __init__(self, restaurant_name, cuisine_type, availability):
        """Initialize the restaurant."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.availability = availability
        self.number_served = 0

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        print(f"\nThis is {self.restaurant_name.title()}.")
        print(f"It's a {self.cuisine_type.title()} restaurant.")

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        print(f"Restaurant is now {self.availability}.")

    def set_number_served(self, number_served):
        """Allow user to set the number of customers that have been served."""
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        """Allow user to increment the number of customers served."""
        self.number_served += additional_served

new_restaurant = Restaurant('hi ho', 'chinese', 'open')

print(new_restaurant.restaurant_name.title())
print(new_restaurant.cuisine_type.title())

new_restaurant.describe_restaurant()
new_restaurant.open_restaurant()

print(f"\nNumber served: {new_restaurant.number_served}")
new_restaurant.number_served = 5
print(f"\nNumber served: {new_restaurant.number_served}")

new_restaurant.set_number_served(25)
print(f"\nNumber served: {new_restaurant.number_served}")

new_restaurant.increment_number_served(20)
print(f"\nNumber served: {new_restaurant.number_served}")
