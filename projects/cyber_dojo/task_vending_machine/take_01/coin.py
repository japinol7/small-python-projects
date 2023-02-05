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


class Coin:
    def __init__(self, diameter, thickness, weight):
        self.diameter = diameter
        self.thickness = thickness
        self.weight = weight
        self.type = None

        self._compute_type()

    def _compute_type(self):
        for key, val in COIN_STATS.items():
            if val == (self.diameter, self.thickness, self.weight):
                self.type = key
                return
        self.type = CoinType.NONE
