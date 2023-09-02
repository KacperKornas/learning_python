import unittest
from city_functions import city_country


class TestCityCountry(unittest.TestCase):
    """Test for 'city_functions.py'"""

    def test_city_country(self):
        """Do output string like 'Santiago Chile' work?"""
        output_string = city_country('santiago', 'chile')
        self.assertEqual(output_string, 'Santiago Chile')

    def test_city_country_population(self):
        """Do output string like 'Santiago Chile - population 5000000' work?"""
        output_string = city_country('santiago', 'chile', 5000000)
        self.assertEqual(output_string, 'Santiago Chile - population 5000000')


if __name__ == '__main__':
    unittest.main()
