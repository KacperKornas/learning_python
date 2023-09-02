import unittest
from _11_3_employee import Employee


class TestEmployee(unittest.TestCase):
    """Tests for the class Employee"""

    def setUp(self):
        """Create an employee instance for each test method."""
        self.eric_goffin = Employee('Eric', 'Goffin', 120000)

    def test_give_default_raise(self):
        """Test to see if a simple raise will work."""
        self.eric_goffin.give_raise()
        self.assertEqual(self.eric_goffin.salary, 125000)

    def test_give_custom_raise(self):
        """Test to see if a custom raise will work."""
        self.eric_goffin.give_raise(10000)
        self.assertEqual(self.eric_goffin.salary, 130000)
