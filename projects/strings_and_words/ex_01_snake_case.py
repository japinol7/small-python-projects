from collections import namedtuple

from utils.utils import print_test_result

import re


def convert_to_snake_case(str_):
    res = ''.join((ch if (ch.isalpha() or ch.isnumeric()) else '_') for ch in str_.lower())
    res = re.sub(r'\_+', '_', res)
    return res


if __name__ == '__main__':
    def check_test_some_cases():
        failed = 0
        TestCaseMapping = namedtuple('test_case_mapping', ['input_val', 'expected'])
        test_cases = {
            1: TestCaseMapping(
                "We %!looked at the lovely*-sunset", "we_looked_at_the_lovely_sunset"),
            2: TestCaseMapping(
                "a 1 b 2 c % 3-d/4", "a_1_b_2_c_3_d_4"),
            3: TestCaseMapping(
                "I bought 2 tickets", "i_bought_2_tickets"),
            4: TestCaseMapping(
                "To Choose what we are%$&to be. This/·is the privilege and the risk of being human",
                "to_choose_what_we_are_to_be_this_is_the_privilege_and_the_risk_of_being_human"),
        }
        for input_val, expected in test_cases.values():
            result = convert_to_snake_case(input_val)
            failed += print_test_result(result, expected)
        print(f"{'-' * 25}\nTests FAILED: {failed}")
    check_test_some_cases()
