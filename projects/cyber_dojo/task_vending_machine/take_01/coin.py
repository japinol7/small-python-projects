from collections import namedtuple
from enum import Enum


class CoinType(Enum):
    NONE = 0
    NICKEL = 1
    DIME = 2
    QUARTER = 3


# We measure diameter and thickness in mm., and weight as mass in grams
CoinStats = namedtuple('coin_stats', ['diameter', 'thickness', 'weight'])
COIN_STATS = {
    CoinType.NICKEL: CoinStats(21.21, 1.95, 5),
    CoinType.DIME: CoinStats(17.91, 1.35, 2.268),
    CoinType.QUARTER: CoinStats(24.257, 1.956, 5.67),
    }

COIN_VALUES = {
    CoinType.NONE:  0,
    CoinType.NICKEL: 0.05,
    CoinType.DIME:  0.10,
    CoinType.QUARTER:  0.25,
    }

COIN_NAMES = {
    CoinType.NONE:  '',
    CoinType.NICKEL: 'Nickel',
    CoinType.DIME:  'Dime',
    CoinType.QUARTER:  'Quarter',
    }


class Coin:
    def __init__(self, diameter, thickness, weight):
        self.diameter = diameter
        self.thickness = thickness
        self.weight = weight
        self.type = None
        self.value = 0

        self._compute_type()
        self._compute_value()

    def _compute_type(self):
        self.type = Coin.get_coin_type(self)

    def _compute_value(self):
        self.value = COIN_VALUES[self.type]

    @staticmethod
    def get_coin_stats(coin_type):
        return COIN_STATS[coin_type]

    @staticmethod
    def get_coin_type(coin):
        for key, val in COIN_STATS.items():
            if val == (coin.diameter, coin.thickness, coin.weight):
                return key
        return CoinType.NONE

    def __str__(self):
        return f"type: {self.type.name} value: {self.value} " \
               f"stats: {self.diameter}, {self.thickness}, {self.weight}"

    def __repr__(self):
        return f"{self.__class__.__name__}("\
               f"{self.diameter}, {self.thickness}, {self.weight})"
