from itertools import chain, combinations


def powerset(iterable, min_items=0, max_items=None):
    """Examples:
    powerset([1, 2, 3]) --> [(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]
    powerset([1, 2, 3], min_items=2, max_items=2) --> [(1, 2), (1, 3), (2, 3)]
    """
    s = list(iterable)
    if not max_items or max_items > len(s):
        max_items = len(s)
    if min_items < 0:
        min_items = 0
    return chain.from_iterable(combinations(s, r) for r in range(min_items, max_items + 1))


if __name__ == '__main__':
    res = powerset([1, 2, 3])
    print(list(res))
    res = powerset([1, 2, 3], min_items=2, max_items=2)
    print(list(res))
