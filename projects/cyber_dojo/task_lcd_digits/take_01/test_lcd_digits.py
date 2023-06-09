from enum import Enum

import pytest

from lcd_digits import LCDDigits, LCDDigitsException
from lcd_digit_cell import CELL_H, CELL_V, CELL_O

TEST_CELL_H = '_'
TEST_CELL_V = '|'
TEST_CELL_O = '.'

DIGITS_REPR_0 = '._.\n'\
                '|.|\n'\
                '|_|\n'

DIGITS_REPR_1 = '...\n'\
                '..|\n'\
                '..|\n'

DIGITS_REPR_2 = '._.\n'\
                '._|\n'\
                '|_.\n'

DIGITS_REPR_910 = '._. ... ._.\n'\
                  '|_| ..| |.|\n'\
                  '..| ..| |_|\n'


class TestLCDDigits:
    @pytest.mark.parametrize('num, expected', [
        (0, DIGITS_REPR_0),
        (1, DIGITS_REPR_1),
        (2, DIGITS_REPR_2),
        # (910, LCD_DIGITS_REPR_FOR_910),
        ])
    def test_generate_anagrams(self, num, expected):
        result = LCDDigits.generate(num)
        result = self._replace_lcd_digit_cells(digit_cell_str=result)
        assert result == expected

    def _replace_lcd_digit_cells(self, digit_cell_str):
        return digit_cell_str.\
            replace(CELL_H, TEST_CELL_H).\
            replace(CELL_V, TEST_CELL_V).\
            replace(CELL_O, TEST_CELL_O)

    def test_negative_num_should_raise_exception(self):
        with pytest.raises(LCDDigitsException):
            LCDDigits.generate(-1)

    def test_non_numeric_arg_should_raise_exception(self):
        with pytest.raises(LCDDigitsException):
            LCDDigits.generate('1')
