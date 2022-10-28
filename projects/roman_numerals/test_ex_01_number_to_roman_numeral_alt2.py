import pytest

from ex_01_number_to_roman_numeral_alt2 import convert_to_roman_numeral


@pytest.mark.parametrize("arabic_num, roman_numeral_num", [
    (23, 'XXIII'), (884, 'DCCCLXXXIV'), (1995, 'MCMXCV'),
    (999, 'CMXCIX'), (36, 'XXXVI'), (3017, 'MMMXVII'),
    (994, 'CMXCIV'), (4978, 'MMMMCMLXXVIII'), (4999, 'MMMMCMXCIX'),
    (0, ''), (52000, ''), ])
def test_computer_player_move__one_cell_left(arabic_num, roman_numeral_num):
    result = convert_to_roman_numeral(arabic_num)
    expected = roman_numeral_num
    assert result == expected
