import unittest
import PrimeFactors as PrimeFactorsClass


class TestPrimeFactors(unittest.TestCase):
    def test_one_returns_empty_list(self):
        expected = []
        pf = PrimeFactorsClass
        actual = pf.PrimeFactors.calculate_primes(self, 0)

        self.assertEqual(expected, actual)

    def test_two_returns_just_two(self):
        expected = [2]
        pf = PrimeFactorsClass
        actual = pf.PrimeFactors.calculate_primes(self, 2)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
