from collections.abc import Sequence


def sw_max_subarray_sum_of_size_k_naive(
        nums: Sequence[int], k: int
) -> int | float:
    max_sum = float('-inf')
    for i in range(0, len(nums) - k + 1):
        current_sum = sum(nums[i: i + k])
        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum


def sw_max_subarray_sum_of_size_k(
        nums: Sequence[int], k: int
) -> int:
    current_sum = 0
    for i in range(0, k):
        current_sum += nums[i]

    max_sum = current_sum
    for i in range(0, len(nums) - k):
        current_sum -= nums[i]
        current_sum += nums[i + k]
        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum


def main():
    data = [92, 41, 542, 878, 12, 41, -32, 45, -522, 769, 689,
            340, 41, 1625, 34, 54, 1000, 33, -127, 321]

    rv_naive = sw_max_subarray_sum_of_size_k_naive(data, 3)
    rv = sw_max_subarray_sum_of_size_k(data, 3)
    expected = 2006
    print(f"Result: {rv}")
    assert rv_naive == rv == expected


if __name__ == '__main__':
    main()
