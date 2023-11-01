from collections.abc import Iterable

# We do not use math.inf because mypy complaints with a type error,
# and we do not want to declare the return type of the function this way: int | float
MAX_INT_VALUE: int = 99999999


def get_number_closest_to_zero(nums: Iterable[int]) -> int:
    if not nums:
        return 0

    if not isinstance(nums, Iterable):
        raise TypeError(f"Input_vals must be an iterable instead of: {type(nums)}.")

    min_positive = min(filter(lambda x: x >= 0, nums), default=MAX_INT_VALUE)
    min_negative = min(filter(lambda x: x < 0, nums), default=-MAX_INT_VALUE)

    return min_positive if min_positive < -min_negative else min_negative
