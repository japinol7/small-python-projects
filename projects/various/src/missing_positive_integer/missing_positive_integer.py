from collections.abc import Iterable

MAX_N = 1_000_000


def missing_positive_integer(list_: Iterable) -> int:
    res = 0
    excluded_values = set(list_)
    for res in range(1, MAX_N + 1):
        if res not in excluded_values:
            break
    return res
