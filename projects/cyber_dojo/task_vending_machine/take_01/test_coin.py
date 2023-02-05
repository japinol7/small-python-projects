import pytest

from coin import Coin, CoinType


class TestCoin:
    @pytest.mark.parametrize('diameter, thickness, weight, expected', [
        (21.21, 1.95, 5, CoinType.NICKEL),
        (17.91, 1.35, 2.268, CoinType.DIME),
        (24.257, 1.956, 5.67, CoinType.QUARTER),
        (23, 2, 5, CoinType.NONE),
        (21, 1.95, 5, CoinType.NONE),
        (0, 0, 0, CoinType.NONE),
        ])
    def test_compute_type(self, diameter, thickness, weight, expected):
        result = Coin(diameter, thickness, weight).type
        assert result == expected
