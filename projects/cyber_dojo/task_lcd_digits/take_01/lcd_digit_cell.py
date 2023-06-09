from enum import Enum


class LCDDigitCell(str, Enum):
    HORIZONTAL = '_'
    VERTICAL = '|'
    OFF = '.'


CELL_H = LCDDigitCell.HORIZONTAL
CELL_V = LCDDigitCell.VERTICAL
CELL_O = LCDDigitCell.OFF

DIGITS_0 = f"{CELL_O}{CELL_H}{CELL_O}\n" \
           f"{CELL_V}{CELL_O}{CELL_V}\n" \
           f"{CELL_V}{CELL_H}{CELL_V}\n"

DIGITS_1 = f"{CELL_O}{CELL_O}{CELL_O}\n" \
           f"{CELL_O}{CELL_O}{CELL_V}\n" \
           f"{CELL_O}{CELL_O}{CELL_V}\n"

DIGITS_2 = f"{CELL_O}{CELL_H}{CELL_O}\n" \
           f"{CELL_O}{CELL_H}{CELL_V}\n" \
           f"{CELL_V}{CELL_H}{CELL_O}\n"


NUM_TO_LCD_DIGIT_MAPPING = {
    0: DIGITS_0,
    1: DIGITS_1,
    2: DIGITS_2,
    }
