import pytest

from calculate_factors import calculate_factors


@pytest.mark.parametrize("input_val, expected", [
    (5, (1, 5)),
    (6, (1, 2, 3, 6)),
    (15, (1, 3, 5, 15)),
    (16, (1, 2, 4, 8, 16)),
    (24, (1, 2, 3, 4, 6, 8, 12, 24)),
    (512, (1, 2, 4, 8, 16, 32, 64, 128, 256, 512)),
    (12400, (1, 2, 4, 5, 8, 10, 16, 20, 25, 31, 40, 50, 62,
             80, 100, 124, 155, 200, 248, 310, 400, 496, 620,
             775, 1240, 1550, 2480, 3100, 6200, 12400)),
    ])
def test_calculate_factors(input_val, expected):
    assert tuple(calculate_factors(input_val)) == expected
