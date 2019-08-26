import unittest
import PrimeFactors


class TestPrimeFactors(unittest.TestCase):
    def test_zero_returns_zero(self):
        expected = []
        actual = []

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
