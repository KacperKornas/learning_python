class User():
    """A class representing a user."""

    def __init__(self, first_name, last_name, age):
        """Initialize a user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age

    def describe_user(self):
        """Display a summary of user."""
        print(f"\nThis is a {self.first_name} {self.last_name}.")
        print(f"{self.first_name} is {self.age} years old.")

    def greet_user(self):
        """Display greetings to the user."""
        print(f"Hello {self.first_name} {self.last_name}!")
