from collections.abc import Sequence

from tools.time_it.time_it import time_it


def search_item_index(list_: Sequence[int], target: int):
    """Returns the position of the target number in an ordered list if exists.
    Otherwise, it returns -1.
    It implements the binary search algorithm.
    """
    low, high = 0, len(list_) - 1

    while low <= high:
        middle = low + (high - low) // 2
        if list_[middle] == target:
            return middle
        if list_[middle] < target:
            low = middle + 1
        else:
            high = middle - 1
    return -1


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
