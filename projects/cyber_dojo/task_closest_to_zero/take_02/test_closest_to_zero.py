import pytest

from closest_to_zero import get_number_closest_to_zero


@pytest.mark.parametrize('input_vals, expected', [
    ([], 0),
    ([2], 2),
    ([-3], -3),
    ([15, 8, 22], 8),
    ([5, -8], 5),
    ([5, 7, -5, -8], 5),
    ([5, 2, 7, -8, 2, 9], 2),
    ((5, -8), 5),
    ((x for x in range(1)), 0),
    ((x for x in range(4, 14, 3)), 4),
    ])
def test_number_closest_to_zero(input_vals, expected):
    assert get_number_closest_to_zero(input_vals) == expected


def test_wrong_type_input_vals_must_raise_exception():
    """When input_vals is not an iterable must raise a TypeError exception."""
    with pytest.raises(TypeError):
        get_number_closest_to_zero(2)
