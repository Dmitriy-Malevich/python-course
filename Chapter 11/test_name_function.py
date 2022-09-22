import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Тесты для 'name_function.py'."""

    def test_first_last_name(self):
        """Имена вида 'Дмитрий Малевич' работают правильно?"""
        formatted_name = get_formatted_name('дмитрий', 'малевич')
        self.assertEqual(formatted_name, 'Дмитрий Малевич')
    def test_first_last_middle_name(self):
        """Работают ли такие имена, как 'Малевич Дмитрий Леонидович'?"""
        formatted_name = get_formatted_name('малевич', 'дмитрий', 'леонидович')
        self.assertEqual(formatted_name, 'Малевич Дмитрий Леонидович')
unittest.main()
