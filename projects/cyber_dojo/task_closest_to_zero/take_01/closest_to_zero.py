from collections.abc import Iterable
import math


def get_number_closest_to_zero(nums: Iterable[int]) -> int | float:
    if not nums:
        return 0

    if not isinstance(nums, Iterable):
        raise TypeError("Input_vals must be an iterable.")

    min_positive = min((x for x in nums if x >= 0), default=math.inf)
    min_negative = min((x for x in nums if x < 0), default=-math.inf)

    return min_positive if min_positive < -min_negative else min_negative
