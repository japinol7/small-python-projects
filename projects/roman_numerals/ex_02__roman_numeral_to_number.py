from utils.utils import print_test_result

ROMAN_NUMERAL_MAPPING = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
    }


def convert_roman_numeral_to_number(roman_numeral):
    roman_mapping = ROMAN_NUMERAL_MAPPING
    num = 0
    for i in range(len(roman_numeral)):
        if i != len(roman_numeral) - 1 and roman_mapping[roman_numeral[i]] < roman_mapping[roman_numeral[i + 1]]:
            num -= roman_mapping[roman_numeral[i]]
            continue
        num += roman_mapping[roman_numeral[i]]
    return num


if __name__ == '__main__':
    from collections import namedtuple
    def check_test_some_cases():
        failed = 0
        TestCaseMapping = namedtuple('test_case_mapping', ['input_val', 'expected'])
        test_cases = {
            1: TestCaseMapping(
                'XXIII', 23),
            2: TestCaseMapping(
                'DCCCLXXXIV', 884),
            3: TestCaseMapping(
                'MCMXCV', 1995),
            4: TestCaseMapping(
                'CMXCIX', 999),
            5: TestCaseMapping(
                'XXXVI', 36),
            6: TestCaseMapping(
                'MMMXVII', 3017),
            7: TestCaseMapping(
                'CMXCIV', 994),
            8: TestCaseMapping(
                'MMMMCMLXXVIII', 4978),
            }
        for input_val, expected in test_cases.values():
            result = convert_roman_numeral_to_number(input_val)
            failed += print_test_result(result, expected)
        print(f"{'-' * 25}\nTests FAILED: {failed}")
    check_test_some_cases()
