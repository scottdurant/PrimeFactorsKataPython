class PrimeFactors:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def calculate_primes(self, given_number):
        result = []
        if given_number == 2:
            result.append(2)
        if given_number == 3:
            result.append(3)
        return result
