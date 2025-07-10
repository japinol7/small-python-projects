from typing import Iterable, Optional

MAX_INT_VALUE: int = 99999999


def get_number_closest_to_zero(nums: Iterable[int]) -> int:
    if not nums:
        return 0

    closest_pos = min_val((x for x in nums if x >= 0), default=MAX_INT_VALUE)
    closest_neg = max_val((x for x in nums if x < 0), default=-MAX_INT_VALUE)
    closest = min_val([closest_pos, -closest_neg])

    return closest if closest == closest_pos else closest_neg


def min_val(iterable: Iterable[int], default: Optional[int] = None) -> Optional[int]:
    if not iterable and not default:
        raise ValueError("Empty iterable")
    if not iterable:
        return default

    low = MAX_INT_VALUE
    for val in iterable:
        if val < low:
            low = val
    return low


def max_val(iterable: Iterable[int], default: Optional[int] = None) -> Optional[int]:
    if not iterable and not default:
        raise ValueError("Empty iterable")
    if not iterable:
        return default

    high = -MAX_INT_VALUE
    for val in iterable:
        if val > high:
            high = val
    return high
