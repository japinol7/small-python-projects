from collections.abc import Iterable, Sequence
import math


def get_number_closest_to_zero(input_vals: Iterable[int]) -> int:
    if not input_vals:
        return 0

    if not isinstance(input_vals, Iterable):
        raise TypeError(f"Input_vals parameter must be an iterable.")

    if isinstance(input_vals, Sequence) and len(input_vals) == 1:
        return input_vals[0]

    input_vals = sorted(input_vals)

    left_zero_vals = list(filter(lambda x: x < 0, input_vals[:]))
    min_left_val = -min(left_zero_vals) if left_zero_vals else math.inf

    right_zero_vals = list(filter(lambda x: x >= 0, input_vals[:]))
    min_right_val = min(right_zero_vals) if right_zero_vals else math.inf

    are_equal = min_right_val == min_left_val
    return min_right_val if are_equal else min(min_left_val, min_right_val)
