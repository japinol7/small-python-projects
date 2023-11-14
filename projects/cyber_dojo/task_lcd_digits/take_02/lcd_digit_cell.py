from enum import Enum


class LCDDigitCell(str, Enum):
    HORIZONTAL = '_'
    VERTICAL = '|'
    OFF = '.'


CELL_H = LCDDigitCell.HORIZONTAL
CELL_V = LCDDigitCell.VERTICAL
CELL_O = LCDDigitCell.OFF
SEPARATOR = ' '

DIGITS_0 = f"{CELL_O.value}{CELL_H.value}{CELL_O.value}%s" \
           f"{CELL_V.value}{CELL_O.value}{CELL_V.value}%s" \
           f"{CELL_V.value}{CELL_H.value}{CELL_V.value}%s"

DIGITS_1 = f"{CELL_O.value}{CELL_O.value}{CELL_O.value}%s" \
           f"{CELL_O.value}{CELL_O.value}{CELL_V.value}%s" \
           f"{CELL_O.value}{CELL_O.value}{CELL_V.value}%s"

DIGITS_2 = f"{CELL_O.value}{CELL_H.value}{CELL_O.value}%s" \
           f"{CELL_O.value}{CELL_H.value}{CELL_V.value}%s" \
           f"{CELL_V.value}{CELL_H.value}{CELL_O.value}%s"

DIGITS_3 = f"{CELL_O.value}{CELL_H.value}{CELL_O.value}%s" \
           f"{CELL_O.value}{CELL_H.value}{CELL_V.value}%s" \
           f"{CELL_O.value}{CELL_H.value}{CELL_V.value}%s"

DIGITS_4 = f"{CELL_O.value}{CELL_O.value}{CELL_O.value}%s" \
           f"{CELL_V.value}{CELL_H.value}{CELL_V.value}%s" \
           f"{CELL_O.value}{CELL_O.value}{CELL_V.value}%s"

DIGITS_5 = f"{CELL_O.value}{CELL_H.value}{CELL_O.value}%s" \
           f"{CELL_V.value}{CELL_H.value}{CELL_O.value}%s" \
           f"{CELL_O.value}{CELL_H.value}{CELL_V.value}%s"

DIGITS_6 = f"{CELL_O.value}{CELL_H.value}{CELL_O.value}%s" \
           f"{CELL_V.value}{CELL_H.value}{CELL_O.value}%s" \
           f"{CELL_V.value}{CELL_H.value}{CELL_V.value}%s"

DIGITS_7 = f"{CELL_O.value}{CELL_H.value}{CELL_O.value}%s" \
           f"{CELL_O.value}{CELL_O.value}{CELL_V.value}%s" \
           f"{CELL_O.value}{CELL_O.value}{CELL_V.value}%s"

DIGITS_8 = f"{CELL_O.value}{CELL_H.value}{CELL_O.value}%s" \
           f"{CELL_V.value}{CELL_H.value}{CELL_V.value}%s" \
           f"{CELL_V.value}{CELL_H.value}{CELL_V.value}%s"

DIGITS_9 = f"{CELL_O.value}{CELL_H.value}{CELL_O.value}%s" \
           f"{CELL_V.value}{CELL_H.value}{CELL_V.value}%s" \
           f"{CELL_O.value}{CELL_O.value}{CELL_V.value}%s"


NUM_TO_LCD_DIGIT_MAPPING = {
    0: DIGITS_0,
    1: DIGITS_1,
    2: DIGITS_2,
    3: DIGITS_3,
    4: DIGITS_4,
    5: DIGITS_5,
    6: DIGITS_6,
    7: DIGITS_7,
    8: DIGITS_8,
    9: DIGITS_9,
    }
