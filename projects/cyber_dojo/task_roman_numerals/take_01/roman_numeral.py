MIN_NUMBER = 1
MAX_NUMBER = 4999
ROMAN_NUMERAL_MAPPING = {
    1000: 'M',
    900: 'CM',
    500: 'D',
    400: 'CD',
    100: 'C',
    90: 'XC',
    50: 'L',
    40: 'XL',
    10: 'X',
    9: 'IX',
    5: 'V',
    4: 'IV',
    1: 'I',
    }


def _convert_to_roman_numeral(num):
    if num < MIN_NUMBER or num > MAX_NUMBER:
        return []
    for key in ROMAN_NUMERAL_MAPPING:
        x = num // key
        yield ROMAN_NUMERAL_MAPPING[key] * x
        num -= x * key
        if num <= 0:
            break


def convert_to_roman_numeral(number):
    return ''.join(x for x in _convert_to_roman_numeral(number))
