class PrimeFactors:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def calculate_primes(self, given_number):
        result = []
        divisor = 2

        if given_number == 1:
            return result

        while given_number != 1:
            if given_number % divisor == 0:
                result.append(divisor)
                given_number = given_number / divisor
            else:
                result.append(given_number)
                return result

        return result
