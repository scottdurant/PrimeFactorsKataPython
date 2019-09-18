import unittest
import PrimeFactors as PrimeFactorsClass


class TestPrimeFactors(unittest.TestCase):
    def test_one_returns_empty_list(self):
        expected = []
        pf = PrimeFactorsClass
        actual = pf.PrimeFactors.calculate_primes(self, 1)

        self.assertEqual(expected, actual)

    def test_two_returns_just_two(self):
        expected = [2]
        pf = PrimeFactorsClass
        actual = pf.PrimeFactors.calculate_primes(self, 2)

        self.assertEqual(expected, actual)

    def test_three_returns_just_three(self):
        expected = [3]
        pf = PrimeFactorsClass
        actual = pf.PrimeFactors.calculate_primes(self, 3)

        self.assertEqual(expected, actual)

    def test_four_returns_two_and_two(self):
        expected = [2, 2]
        pf = PrimeFactorsClass
        actual = pf.PrimeFactors.calculate_primes(self, 4)

        self.assertEqual(expected, actual)

    def test_eight_returns_two_two_and_two(self):
        expected = [2, 2, 2]
        pf = PrimeFactorsClass
        actual = pf.PrimeFactors.calculate_primes(self, 8)

        self.assertEqual(expected, actual)

    def test_ten_returns_two_and_five(self):
        expected = [2, 5]
        pf = PrimeFactorsClass
        actual = pf.PrimeFactors.calculate_primes(self, 10)

        self.assertEqual(expected, actual)

    def test_eighteen_returns_two_and_three_and_three(self):
        expected = [2, 3, 3]
        pf = PrimeFactorsClass
        actual = pf.PrimeFactors.calculate_primes(self, 18)

        self.assertEqual(expected, actual)



if __name__ == '__main__':
    unittest.main()
