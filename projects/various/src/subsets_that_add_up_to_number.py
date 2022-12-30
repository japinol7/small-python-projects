# TODO: Inefficient version. Must improve performance.

import itertools

from time_it.time_it import time_it


def list_permutations(nums):
    return list(itertools.permutations(nums))


def get_subsets_that_add_up_to_number(numbers, target, partial=None, partial_sum=0):
    """Gets subsets that add up to a given number."""
    if partial is None:
        partial = []
    if partial_sum == target:
        yield partial
    if partial_sum >= target:
        return
    for i, n in enumerate(numbers):
        remaining = numbers[i + 1:]
        yield from get_subsets_that_add_up_to_number(
            remaining, target, partial + [n], partial_sum + n)


def main(target, n_chunks):
    nums = tuple(range(0, target + 1)) * n_chunks
    res = get_subsets_that_add_up_to_number(nums, target)
    res = [tuple(x) for x in res if len(x) == n_chunks]
    res = [list_permutations(x) for x in res]
    res = set(item for sublist in res for item in sublist)
    return res


if __name__ == '__main__':
    # input_target_num = 20
    input_target_num = 7
    input_n_chunks = 3
    result = time_it(main, input_target_num, input_n_chunks)
    print(f'Res: {result}')
