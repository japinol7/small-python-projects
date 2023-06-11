import pytest

from prime_factors import PrimeFactors, PrimeFactorsException


class TestPrimeFactors:

    @pytest.mark.parametrize('num, expected', [
        (0, [0]),
        (1, [1]),
        (2, [2]),
        (3, [3]),
        (4, [2, 2]),
        (6, [2, 3]),
        (9, [3, 3]),
        (12, [2, 2, 3]),
        (15, [3, 5]),
        (48510, [2, 3, 3, 5, 7, 7, 11]),
        ])
    def test_prime_factors(self, num, expected):
        result = list(PrimeFactors.generate_factors(num))
        assert result == expected

    def test_factors_of_negative_num_should_raise_exception(self):
        with pytest.raises(PrimeFactorsException):
            PrimeFactors.generate_factors(-1)
