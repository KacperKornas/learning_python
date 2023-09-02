class Employee:
    """Class representing an employee"""

    def __init__(self, first, last, salary):
        """Initialize the employee."""
        self.first = first.title()
        self.last = last.title()
        self.salary = salary

    def give_raise(self, raise_salary=5000):
        """Give the employee a rise."""
        self.salary += raise_salary

