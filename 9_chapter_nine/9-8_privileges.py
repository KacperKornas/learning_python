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
        self.privileges = Privileges()

class Privileges():
    """A class display privileges."""

    def __init__(self, privileges=[]):
        """Initialize privileges."""
        self.privileges = privileges

    def show_privileges(self):
        """A method display privileges."""
        if self.privileges:
            print("This user can:")
            for privilege in self.privileges:
                print(f"-{privilege}")
        else:
            print("This user have no privileges.")

karol = Admin('karol', 'kaczyński', 42)
karol.describe_user()

karol.privileges.show_privileges()
karol_privileges = [
    'add comment',
    'delate comment',
    'ban user'
]
karol.privileges.privileges = karol_privileges
karol.privileges.show_privileges()





