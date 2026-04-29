from collections.abc import Sequence


def sw_count_subarray_target_sum_of_size_k(
        nums: Sequence[int], k: int, target: int
) -> int:
    current_sum = 0
    for i in range(0, k):
        current_sum += nums[i]

    count = 1 if current_sum == target else 0

    for i in range(0, len(nums) - k):
        current_sum -= nums[i]
        current_sum += nums[i + k]
        if current_sum == target:
            count += 1

    return count


def main():
    data = [92, 41, 542, 878, 12, 41, -32, 45, -522, 769, 689,
            340, 41, 1625, 34, 54, 1000, 33, -127, 88, 900, 100]

    rv = sw_count_subarray_target_sum_of_size_k(data, 3, 1088)
    expected = 2
    print(f"Result: {rv}")
    assert rv == expected


if __name__ == '__main__':
    main()
