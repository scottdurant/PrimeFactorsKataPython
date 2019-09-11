class PrimeFactors:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def calculate_primes(self, given_number):
        result = []

        if given_number == 1:
            return result

        while given_number != 1:
            if given_number % 2 == 0:
                result.append(2)
                given_number = given_number / 2

            if given_number == 3:
                result.append(3)
                given_number = given_number / 3

        return result
