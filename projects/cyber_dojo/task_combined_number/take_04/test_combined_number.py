import pytest

from combined_number import CombinedNumber


class TestCombinedNumber:
    @pytest.mark.parametrize('nums, expected', [
        ([50, 2, 1, 9], '95021'),
        ([5, 50, 56], '56550'),
        ([420, 42, 423], '42423420'),
        ([], ''),
        ])
    def test_combined_number(self, nums, expected):
        result = CombinedNumber.combined_number(nums)
        assert result == expected
