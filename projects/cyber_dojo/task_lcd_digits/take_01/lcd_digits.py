from lcd_digit_cell import NUM_TO_LCD_DIGIT_MAPPING, SEPARATOR


class LCDDigitsException(Exception):
    pass


class LCDDigits:
    @staticmethod
    def generate(num, separator=SEPARATOR):
        if not isinstance(num, int) or num < 0:
            raise LCDDigitsException

        if NUM_TO_LCD_DIGIT_MAPPING.get(num):
            return NUM_TO_LCD_DIGIT_MAPPING[num] % ('\n', '\n', '\n')

        digits = LCDDigits._generate_multiple_digits(num, separator)
        return ''.join(digits)

    @staticmethod
    def _generate_multiple_digits(num, separator):
        digits_top = []
        digits_mid = []
        digits_bottom = []
        num_len = len(str(num))
        for i, digit in enumerate(str(num)):
            cur_separator = '\n' if i == num_len - 1 else separator
            digits_top += [NUM_TO_LCD_DIGIT_MAPPING[int(digit)][:5] % cur_separator]
            digits_mid += [NUM_TO_LCD_DIGIT_MAPPING[int(digit)][5:10] % cur_separator]
            digits_bottom += [NUM_TO_LCD_DIGIT_MAPPING[int(digit)][10:15] % cur_separator]

        digits = []
        digits.extend(digits_top)
        digits.extend(digits_mid)
        digits.extend(digits_bottom)
        return digits
