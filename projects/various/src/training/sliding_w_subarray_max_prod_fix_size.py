from collections.abc import Sequence


def sw_max_subarray_product_of_size_k(
        nums: Sequence[int], k: int
) -> int:
    current_product = 1
    for i in range(0, k):
        current_product *= nums[i]
    max_product = current_product

    for i in range(0, len(nums) - k):
        current_product /= nums[i]
        current_product *= nums[i + k]
        max_product = max(max_product, current_product)

    return int(max_product)


def main():
    data = [92, 41, 542, 878, 12, 41, -32, 45, -522, 769, 689,
            340, 41, 1625, 34, 54, 1000, 33, -127, 321]

    rv = sw_max_subarray_product_of_size_k(data, 3)
    expected = 180145940
    print(f"Result: {rv}")
    assert rv == expected


if __name__ == '__main__':
    main()
