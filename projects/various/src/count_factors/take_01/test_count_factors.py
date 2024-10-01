import pytest

from count_factors import count_factors


@pytest.mark.parametrize("input_val, expected", [
    (5, 2),
    (6, 4),
    (15, 4),
    (16, 5),
    (24, 8),
    (512, 10),
    (12400, 30),
    (1_000_000, 49),
    (2_000_000, 56),
    (5_500_000, 84),
    (20_147_483, 2),
    (5_042_483_640, 96),
    ])
def test_count_factors(input_val, expected):
    assert count_factors(input_val) == expected
