from collections.abc import Generator, Iterable, Sequence
import math


def get_number_closest_to_zero(nums: Iterable[int]) -> int | float:
    if not nums:
        return 0

    if not isinstance(nums, Iterable):
        raise TypeError("Input_vals must be an iterable.")

    if isinstance(nums, Sequence) and len(nums) == 1:
        return nums[0]

    if isinstance(nums, Generator):
        nums = list(nums)

    left_zero_vals = list(filter(lambda x: x < 0, nums))
    min_left_val = -min(left_zero_vals) if left_zero_vals else math.inf

    right_zero_vals = list(filter(lambda x: x >= 0, nums))
    min_right_val = min(right_zero_vals) if right_zero_vals else math.inf

    are_equal = min_right_val == min_left_val
    return min_right_val if are_equal else min(min_left_val, min_right_val)
