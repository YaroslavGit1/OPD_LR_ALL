import unittest
from OPD_LR3and4 import convert_currency, exchange_rates

class TestCurrencyConverter(unittest.TestCase):

    def test_usd_to_eur(self):
        """Проверка конвертации из USD в RUB."""
        result = convert_currency(100, 'USD', 'RUB')
        self.assertAlmostEqual(result, 9000, places=2)

    def test_rub_to_usd(self):
        """Проверка конвертации из RUB в USD."""
        result = convert_currency(100, 'RUB', 'USD')
        self.assertAlmostEqual(result, 1.11, places=2)

    def test_negative_amount(self):
        with self.assertRaises(ValueError):
            convert_currency(-10, 'USD', 'EUR')

    def test_same_currency(self):
        result = convert_currency(123, 'USD', 'USD')
        self.assertAlmostEqual(result, 123.0, places=2)

if __name__ == '__main__':
    unittest.main()
