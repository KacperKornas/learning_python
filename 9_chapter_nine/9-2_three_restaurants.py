class Restaurant():
    """A class representing a restaurant."""

    def __init__(self, restaurant_name, cuisine_type, availability):
        """Initialize the restaurant."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.availability = availability

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        print(f"\nThis is {self.restaurant_name.title()}.")
        print(f"It's a {self.cuisine_type.title()} restaurant.")

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        print(f"Restaurant is now {self.availability}.")

new_restaurant = Restaurant('hi ho', 'chinese', 'open')
old_restaurant = Restaurant('big ben', 'cafe', 'open')
start_restaurant = Restaurant('crim crim', 'ice cream', 'close')

old_restaurant.describe_restaurant()
old_restaurant.open_restaurant()

new_restaurant.describe_restaurant()
new_restaurant.open_restaurant()

start_restaurant.describe_restaurant()
start_restaurant.open_restaurant()


