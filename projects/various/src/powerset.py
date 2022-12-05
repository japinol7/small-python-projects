from itertools import chain, combinations


def powerset(iterable, min_elements=0, max_elements=None):
    """Example:
    powerset([1, 2, 3], 0) --> [(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]
    """
    s = list(iterable)
    if not max_elements:
        max_elements = len(s)
    return chain.from_iterable(combinations(s, r) for r in range(min_elements, max_elements + 1))


if __name__ == '__main__':
    res = powerset([1, 2, 3], 0)
    print(list(res))
