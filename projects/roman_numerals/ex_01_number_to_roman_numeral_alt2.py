from utils.utils import print_test_result

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


def convert_to_roman_numeral(num):
    roman_numeral = []
    for key in ROMAN_NUMERAL_MAPPING:
        x = num // key
        if x > 0:
            roman_numeral += [ROMAN_NUMERAL_MAPPING[key] * x]
            num -= key * x
        if num <= 0:
            break
    return ''.join(roman_numeral)


def main():
    from collections import namedtuple
    def check_test_some_cases():
        failed = 0
        TestCaseMapping = namedtuple('test_case_mapping', ['input_val', 'expected'])
        test_cases = {
            1: TestCaseMapping(
                23, 'XXIII'),
            2: TestCaseMapping(
                884, 'DCCCLXXXIV'),
            3: TestCaseMapping(
                1995, 'MCMXCV'),
            4: TestCaseMapping(
                999, 'CMXCIX'),
            5: TestCaseMapping(
                36, 'XXXVI'),
            6: TestCaseMapping(
                3017, 'MMMXVII'),
            7: TestCaseMapping(
                994, 'CMXCIV'),
            8: TestCaseMapping(
                4978, 'MMMMCMLXXVIII'),
            9: TestCaseMapping(
                0, ''),
            }
        for input_val, expected in test_cases.values():
            result = convert_to_roman_numeral(input_val)
            failed += print_test_result(result, expected)
        print(f"{'-' * 25}\nTests FAILED: {failed}")
    check_test_some_cases()


if __name__ == '__main__':
    main()
