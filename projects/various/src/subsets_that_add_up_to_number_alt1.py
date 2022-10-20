# TODO: Inefficient version. Must improve performance.

import itertools

from time_it.time_it import time_it


def list_permutations(nums):
    return list(itertools.permutations(nums))


def get_subsets_that_add_up_to_number(target, n_chunks):
    """Get subsets that add up to a given number."""
    def _collapse(nums):
        yield nums
        while len(nums) > 1:
            nums = nums[:-2] + [nums[-2] + nums[-1]]
            for prefix in _collapse(nums[:-1]):
                if not prefix or prefix[-1] <= nums[-1]:
                    yield prefix + [nums[-1]]
    return [x for x in list(_collapse([1] * target))]


def main(target, n_chunks):
    res = get_subsets_that_add_up_to_number(target, n_chunks)
    size_chunks_small = []
    for size_chunk in (x for x in res if len(x) < n_chunks):
        size_chunks_small.append(size_chunk + [0] * (n_chunks - len(size_chunk)))
    res = [x for x in res if len(x) == n_chunks]
    res.extend(size_chunks_small)

    res = [list_permutations(x) for x in res]
    res = set(item for sublist in res for item in sublist)
    return res


if __name__ == '__main__':
    # input_target_num = 20
    input_target_num = 7
    input_n_chunks = 3
    result = time_it(main, input_target_num, input_n_chunks)
    print(f'Res: {result}')
