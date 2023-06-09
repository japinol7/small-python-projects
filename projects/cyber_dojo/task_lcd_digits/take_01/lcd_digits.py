# TODO: WIP
from lcd_digit_cell import NUM_TO_LCD_DIGIT_MAPPING


class LCDDigitsException(Exception):
    pass


class LCDDigits:
    @staticmethod
    def generate(num):
        if not isinstance(num, int) or num < 0:
            raise LCDDigitsException

        if NUM_TO_LCD_DIGIT_MAPPING.get(num):
            return NUM_TO_LCD_DIGIT_MAPPING[num]

        return ''
