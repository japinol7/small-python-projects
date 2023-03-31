from typing import List

from config import DECIMALS
from coin import Coin


class CoinDispenserNotEnoughPaymentException(Exception):
    pass


class CoinDispenserCannotProvideExactChangeException(Exception):
    pass


class CoinDispenser:
    def __init__(self, coins: List[Coin]):
        self.coins = coins

    def get_change_coins(self, cost: float, payment: float) -> List[float]:
        """Returns the coins to be returned as change"""
        if payment < cost:
            raise CoinDispenserNotEnoughPaymentException(
                "Payment is less than the cost")

        change_amount = round(payment - cost, DECIMALS)
        change_coins = []
        for coin in sorted(self.coins, key=lambda x: x.value, reverse=True):
            while change_amount >= coin.value:
                change_coins += [coin]
                change_amount -= coin.value

        if change_amount:
            raise CoinDispenserCannotProvideExactChangeException(
                "Cannot provide exact change with the available coins")

        return change_coins
