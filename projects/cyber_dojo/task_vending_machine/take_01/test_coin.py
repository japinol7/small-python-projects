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

    @pytest.mark.parametrize('diameter, thickness, weight, expected', [
        (21.21, 1.95, 5, 0.05),
        (17.91, 1.35, 2.268, 0.1),
        (24.257, 1.956, 5.67, 0.25),
        (23, 2, 5, 0),
        (21, 1.95, 5, 0),
        (0, 0, 0, 0),
        ])
    def test_compute_value(self, diameter, thickness, weight, expected):
        result = Coin(diameter, thickness, weight).value
        assert result == expected

    def test_str_and_repr(self):
        coin = Coin(15.91, 1.35, 2.268)
        assert repr(coin) == 'Coin(15.91, 1.35, 2.268)'
        assert str(coin) == 'type: NONE value: 0 stats: 15.91, 1.35, 2.268'
