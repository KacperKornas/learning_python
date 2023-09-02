from user import User

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



