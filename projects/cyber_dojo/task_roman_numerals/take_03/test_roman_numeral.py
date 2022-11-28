import pytest

from roman_numeral import convert_to_roman_numeral


@pytest.mark.parametrize("arabic_num, roman_numeral_num", [
    (100, 'C'), (200, 'CC'), (400, 'CD'), (47, 'XLVII'),
    (1990, 'MCMXC'), (2008, 'MMVIII'), (99, 'XCIX'),
    (23, 'XXIII'), (884, 'DCCCLXXXIV'), (1995, 'MCMXCV'),
    (999, 'CMXCIX'), (36, 'XXXVI'), (3017, 'MMMXVII'),
    (994, 'CMXCIV'), (4978, 'MMMMCMLXXVIII'), (4999, 'MMMMCMXCIX'),
    (0, ''), (52000, ''),
    ])
def test_computer_player_move__one_cell_left(arabic_num, roman_numeral_num):
    result = convert_to_roman_numeral(arabic_num)
    expected = roman_numeral_num
    assert result == expected
