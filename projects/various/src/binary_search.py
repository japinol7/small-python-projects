from time_it.time_it import time_it


def search_item_index(list_, item):
    """Returns the position of item in the nums list if exists.
    Otherwise, it returns -1.
    Implements the binary search algorithm.
    """
    low = 0
    high = len(list_) - 1

    while low <= high:
        middle = (low + high) // 2
        if list_[middle] == item:
            return middle
        if list_[middle] < item:
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
