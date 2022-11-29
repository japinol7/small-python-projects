import pytest

from leap_year import leap_year


@pytest.mark.parametrize('year, expected', [
    (2001, False),
    (1996, True),
    (1900, False),
    (2000, True),
    (2023, False),
    (2024, True),
    (0, False),
    ])
def test_leap_year(year, expected):
    result = leap_year(year)
    assert result == expected
