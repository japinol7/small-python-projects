from collections.abc import Iterable
import math


def get_number_closest_to_zero(input_vals: Iterable[int]) -> int:
    if not input_vals:
        return 0

    min_positive = min((x for x in input_vals if x >= 0), default=int(math.inf))
    min_negative = min((x for x in input_vals if x < 0), default=-int(math.inf))

    return min_positive if min_positive < -min_negative else min_negative
