import unittest
import PrimeFactors as PrimeFactorsClass


class TestPrimeFactors(unittest.TestCase):
    def test_one_returns_empty_list(self):
        expected = []
        pf = PrimeFactorsClass
        actual = pf.PrimeFactors.calculate_primes(self, 0)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
