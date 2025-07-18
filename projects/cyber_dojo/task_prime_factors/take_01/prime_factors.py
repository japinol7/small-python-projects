class PrimeFactorsException(Exception):
    pass


class PrimeFactors:
    """Generates prime factors of positive numbers."""
    @staticmethod
    def generate_factors(num):
        if num < 0:
            raise PrimeFactorsException(
                "User error. Given number cannot be a negative number.")

        return PrimeFactors._prime_factors(num)

    @staticmethod
    def _prime_factors(num):
        candidate = 2
        while candidate * candidate <= num:
            if num % candidate:
                candidate += 1
                continue
            num //= candidate
            yield candidate

        if num >= 0:
            yield num
