import pytest

from count_coins import CountCoins


class TestCountCoins:
    @pytest.mark.parametrize('amount, value', [
        (0, 0),
        (15, 6),
        (20, 9),
        (25, 13),
        (30, 18),
        (53, 49),
        ])
    def test_changes(self, amount, value):
        result = CountCoins().changes(amount)
        expected = value
        assert result == expected

    def test_changes_100_cents_and_output(self):
        result = CountCoins().changes(100)
        expected = 242
        assert result == expected
        print("Output: \n"
              "How many ways are there to make change for a dollar \n"
              "using these common coins? (1 dollar = 100 cents) \n"
              f"Result: {result}")
