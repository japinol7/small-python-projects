from itertools import chain, combinations


def powerset(iterable, min_element_count):
    """Example: powerset([1, 2, 3], 0) --> [(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]"""
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(min_element_count, len(s) + 1))


if __name__ == '__main__':
    res = powerset([1, 2, 3], 0)
    print(list(res))
