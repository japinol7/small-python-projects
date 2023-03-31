import pytest

from coin import Coin
from coin_dispenser import (
    CoinDispenserNotEnoughPaymentException,
    CoinDispenserCannotProvideExactChangeException)


class TestCoinDispenser:
    def test_get_change_coins_without_change(self, coin_dispenser_with_coins):
        cost = 1.3
        payment = 1.3
        change_coins = coin_dispenser_with_coins.get_change_coins(cost, payment)
        result = str(change_coins)
        expected = '[]'
        assert result == expected

    def test_get_change_coins_without_enough_payment_must_raise_exception(self, coin_dispenser_with_coins):
        with pytest.raises(CoinDispenserNotEnoughPaymentException):
            cost = 1.3
            payment = 1.25
            coin_dispenser_with_coins.get_change_coins(cost, payment)

    def test_get_change_coins_without_exact_change_must_raise_exception(self, coin_dispenser_with_coins):
        with pytest.raises(CoinDispenserCannotProvideExactChangeException):
            cost = 1.3
            payment = 1.85
            coin_dispenser_with_coins.get_change_coins(cost, payment)

    def test_get_change_coins(self, coin_dispenser_with_coins):
        cost = 1.3
        payment = 1.50
        change_coins = coin_dispenser_with_coins.get_change_coins(cost, payment)
        result = str(change_coins)
        expected = str([Coin(17.91, 1.35, 2.268), Coin(17.91, 1.35, 2.268)])
        assert result == expected
        print(f"\nChange coins:{[coin.value for coin in change_coins]}")
