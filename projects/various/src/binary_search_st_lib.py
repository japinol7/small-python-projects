import bisect

from tools.time_it.time_it import time_it


def search_item_index(list_, target):
    """Returns the position of the target number in an ordered list if exists.
    Otherwise, it returns -1.
    It uses the binary search algorithm from the standard library.
    """
    res = bisect.bisect_right(list_, target)
    return res - 1


def main():
    input_item_to_find = 27300103
    input_nums = list(range(100, 50000000, 3))

    print("Start search")
    result = time_it(search_item_index, input_nums, input_item_to_find)
    if result == -1:
        print("Number not found")
        return
    print(f'Res list len: {len(input_nums)}, pos: {result}, number: {input_nums[result]}')


if __name__ == '__main__':
    main()
