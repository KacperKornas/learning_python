class User():
    """A class representing a user."""

    def __init__(self, first_name, last_name, age):
        """Initialize a user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        """Display a summary of user."""
        print(f"\nThis is a {self.first_name} {self.last_name}.")
        print(f"{self.first_name} is {self.age} years old.")

    def greet_user(self):
        """Display greetings to the user."""
        print(f"Hello {self.first_name} {self.last_name}!")

    def increment_login_attempts(self):
        """Increments the value of login attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets the value of login attempts to 0."""
        self.login_attempts = 0

user_1 = User('roberto', 'massimo', 22)
user_1.describe_user()
user_1.greet_user()
print(user_1.login_attempts)
user_1.increment_login_attempts()
print(user_1.login_attempts)
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
print(user_1.login_attempts)
user_1.reset_login_attempts()
print(user_1.login_attempts)
