ROMAN_NUMERAL_MAPPING = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
    }


def _convert_roman_numeral_to_number(roman_numeral):
    roman_mapping = ROMAN_NUMERAL_MAPPING
    num = 0
    for i in range(len(roman_numeral)):
        if i != len(roman_numeral) - 1 and roman_mapping[roman_numeral[i]] < roman_mapping[roman_numeral[i + 1]]:
            num -= roman_mapping[roman_numeral[i]]
            continue
        num += roman_mapping[roman_numeral[i]]
    return num


def reverse_roman(number):
    return _convert_roman_numeral_to_number(number)
