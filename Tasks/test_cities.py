import unittest
from city import get_city_functions

class NamesTestCase(unittest.TestCase):
    """Тесты для '11_1.py'."""
    def test_city_country(self):
        city_functions = get_city_functions('беларусь', 'минск')
        self.assertEqual(city_functions, 'Беларусь, Минск')

    def test_city_country_population(self):
        city_functionss = get_city_functions('беларусь', 'минск', '1000000')
        self.assertEqual(city_functionss, 'Беларусь, Минск -Population 1000000')
unittest.main()
