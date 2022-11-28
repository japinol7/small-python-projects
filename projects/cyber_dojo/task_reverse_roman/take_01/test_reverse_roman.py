import pytest

from reverse_roman import reverse_roman


@pytest.mark.parametrize("arabic_num, roman_numeral_num", [
    ('C', 100), ('CC', 200), ('CD', 400), ('XLVII', 47),
    ('MCMXC', 1990), ('MMVIII', 2008), ('XCIX', 99),
    ('XXIII', 23), ('DCCCLXXXIV', 884), ('MCMXCV', 1995),
    ('CMXCIX', 999), ('XXXVI', 36), ('MMMXVII', 3017),
    ('CMXCIV', 994), ('MMMMCMLXXVIII', 4978), ('MMMMCMXCIX', 4999),
    ('', 0),
    ])
def test_computer_player_move__one_cell_left(arabic_num, roman_numeral_num):
    result = reverse_roman(arabic_num)
    expected = roman_numeral_num
    assert result == expected
