import pytest

from array_to_phone_number import array_to_phone_number


@pytest.mark.parametrize('nums, expected', [
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], '(000) 000-0000'),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], '(123) 456-7890'),
    ([1, 0, 3, 4, 5, 6, 7, 8, 9, 2], '(103) 456-7892'),
    ([1, 5, 1, 0, 5, 3, 7, 7, 9, 1], '(151) 053-7791'),
    (range(10), '(012) 345-6789'),
    ])
def test_array_to_phone_number(nums, expected):
    assert array_to_phone_number(nums) == expected
