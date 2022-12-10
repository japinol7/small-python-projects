import pytest

from calc_stats import CalcStats

STATS_MAPPING = {
    'min': 0,
    'max': 1,
    'len': 2,
    'average': 3,
    }


@pytest.mark.parametrize('nums, expected', [
    ([6, 9, 15, -2, 92, 11], [-2, 92, 6, 21.833333]),
    ([8, 15, -95.13, 47], [-95.13, 47, 4, -6.2825]),
    ([2, 7, 3], [2, 7, 3, 4]),
    ([-2, 5], [-2, 5, 2, 1.5]),
    ([4], [4, 4, 1, 4])
    ])
class TestCalcStats:
    def test_min(self, nums, expected):
        result = CalcStats(nums).min()
        expected = expected[STATS_MAPPING['min']]
        assert result == expected

    def test_max(self, nums, expected):
        result = CalcStats(nums).max()
        expected = expected[STATS_MAPPING['max']]
        assert result == expected

    def test_len(self, nums, expected):
        result = CalcStats(nums).len()
        expected = expected[STATS_MAPPING['len']]
        assert result == expected

    def test_average(self, nums, expected):
        result = CalcStats(nums).average()
        expected = expected[STATS_MAPPING['average']]
        assert result == expected

    def test_calculate(self, nums, expected):
        result = CalcStats(nums).calculate()
        assert result == expected


def test_stats_calculate_empty_list():
    nums = []
    result = CalcStats(nums).calculate()
    expected = []
    assert result == expected


def test_stats_calculate_output():
    nums = [6, 9, 15, -2, 92, 11]
    result = CalcStats(nums).calculate()
    expected = [-2, 92, 6, 21.833333]
    assert result == expected
    print(f'\nStatistics:'
          f'\n{CalcStats.to_str(result)}')
