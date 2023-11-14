from lcd_digit_cell import SEPARATOR

import pytest

from lcd_digits import generate_lcd_digits, LCDDigitsException
from lcd_digit_cell import CELL_H, CELL_V, CELL_O

TEST_CELL_H = '_'
TEST_CELL_V = '|'
TEST_CELL_O = '.'
TEST_SEPARATOR = ' '
TEST_SEPARATOR_BIG = '     '

DIGITS_REPR_0 = '._.\n'\
                '|.|\n'\
                '|_|\n'

DIGITS_REPR_1 = '...\n'\
                '..|\n'\
                '..|\n'

DIGITS_REPR_2 = '._.\n'\
                '._|\n'\
                '|_.\n'

DIGITS_REPR_3 = '._.\n'\
                '._|\n'\
                '._|\n'

DIGITS_REPR_4 = '...\n'\
                '|_|\n'\
                '..|\n'

DIGITS_REPR_5 = '._.\n'\
                '|_.\n'\
                '._|\n'

DIGITS_REPR_6 = '._.\n'\
                '|_.\n'\
                '|_|\n'

DIGITS_REPR_7 = '._.\n'\
                '..|\n'\
                '..|\n'

DIGITS_REPR_8 = '._.\n'\
                '|_|\n'\
                '|_|\n'

DIGITS_REPR_9 = '._.\n'\
                '|_|\n'\
                '..|\n'

DIGITS_REPR_1234567890 = '' \
                  '... ._. ._. ... ._. ._. ._. ._. ._. ._.\n'\
                  '..| ._| ._| |_| |_. |_. ..| |_| |_| |.|\n'\
                  '..| |_. ._| ..| ._| |_| ..| |_| ..| |_|\n'

DIGITS_REPR_1234567890_SEPARATOR_BIG = '' \
                  '...     ._.     ._.     ...     ._.     ._.     ._.     ._.     ._.     ._.\n'\
                  '..|     ._|     ._|     |_|     |_.     |_.     ..|     |_|     |_|     |.|\n'\
                  '..|     |_.     ._|     ..|     ._|     |_|     ..|     |_|     ..|     |_|\n'

DIGITS_REPR_910 = '._. ... ._.\n'\
                  '|_| ..| |.|\n'\
                  '..| ..| |_|\n'


class TestLCDDigits:
    @pytest.mark.parametrize('num, expected', [
        (0, DIGITS_REPR_0),
        (1, DIGITS_REPR_1),
        (2, DIGITS_REPR_2),
        (3, DIGITS_REPR_3),
        (4, DIGITS_REPR_4),
        (5, DIGITS_REPR_5),
        (6, DIGITS_REPR_6),
        (7, DIGITS_REPR_7),
        (8, DIGITS_REPR_8),
        (9, DIGITS_REPR_9),
        (1234567890, DIGITS_REPR_1234567890),
        (910, DIGITS_REPR_910),
        ])
    def test_generate_lcd_digits(self, num, expected):
        result = generate_lcd_digits(num)
        result = self._replace_lcd_digit_cells(digit_cell_str=result)
        result = self._replace_lcd_digit_separators(digit_cell_str=result)
        assert result == expected

    @pytest.mark.parametrize('num, expected', [
        (1234567890, DIGITS_REPR_1234567890_SEPARATOR_BIG),
        ])
    def test_generate_lcd_digits_with_separator_of_5_spaces(self, num, expected):
        separator = '    '
        result = generate_lcd_digits(num, separator)
        result = self._replace_lcd_digit_cells(digit_cell_str=result)
        result = self._replace_lcd_digit_separators(
                      digit_cell_str=result,
                      separator=separator,
                      test_separator=TEST_SEPARATOR_BIG)
        assert result == expected

    def _replace_lcd_digit_cells(self, digit_cell_str):
        return digit_cell_str.\
            replace(CELL_H, TEST_CELL_H).\
            replace(CELL_V, TEST_CELL_V).\
            replace(CELL_O, TEST_CELL_O)

    def _replace_lcd_digit_separators(self, digit_cell_str, separator=SEPARATOR, test_separator=TEST_SEPARATOR):
        return digit_cell_str.replace(separator, test_separator)

    def test_negative_num_should_raise_exception(self):
        with pytest.raises(LCDDigitsException):
            generate_lcd_digits(-1)

    def test_non_numeric_arg_should_raise_exception(self):
        with pytest.raises(LCDDigitsException):
            generate_lcd_digits('1')
