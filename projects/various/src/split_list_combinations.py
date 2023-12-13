import itertools

from tools.time_it.time_it import time_it


def split_list_combinations(nums, n_chunks):
    return [frozenset(i) for i in itertools.combinations(nums, n_chunks)]


def main():
    input_n_chunks, input_nums = 3, [2, 1, 5, 1, 2, 2, 2]
    result = time_it(split_list_combinations, input_nums, input_n_chunks)
    result = set(result)
    print(f'Res: {result}')


if __name__ == '__main__':
    main()
