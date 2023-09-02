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

class Admin(User):
    """A class representing the admin."""

    def __init__(self, first_name, last_name, age):
        """Initialize the Admin."""
        super().__init__(first_name, last_name, age)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        """Show privileges."""
        print("This user can:")
        for privilage in self.privileges:
            print(f"-{privilage}")

admin = Admin('Krzysztof', 'Zięba', 25)
user_1 = User('roberto', 'massimo', 22)
user_1.describe_user()
user_1.greet_user()
admin.describe_user()
admin.show_privileges()