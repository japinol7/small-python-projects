import pytest

from missing_positive_integer import MAX_N, missing_positive_integer


@pytest.mark.parametrize('val, expected', [
    ([], 1),
    ([1, 3, 6, 4, 1, 2, 7], 5),
    ([-1, -3], 1),
    ([1, 2, 3, 5], 4),
    ([1, 3, 6, 4, 1, 2, 5, 7, 6, 555], 8),
    (list(range(-1000_000, MAX_N - 1)), MAX_N - 1),
    (list(range(-1000_000, MAX_N + 2)), MAX_N),
    (list(range(-50, 800_001)), 800_001),
    (range(-50, 80_000), 80_000),
    ])
def test_missing_positive_integer(val, expected):
    assert missing_positive_integer(val) == expected
