import bisect

from time_it.time_it import time_it


def binary_search_position_to_insert(nums, item):
    res = bisect.bisect_left(nums, item)
    return res


def main():
    input_item_to_find, input_nums = 3, [2, 1, 5, 1, 2, 2, 2, 7]
    input_nums = sorted(input_nums)
    print(input_nums)
    result = time_it(binary_search_position_to_insert, input_nums, input_item_to_find)
    print(f'Res: {result}')


if __name__ == '__main__':
    main()