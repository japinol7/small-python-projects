from collections import namedtuple

from utils.utils import print_test_result


def calc_intersection_of_strs_of_ordered_ints(lists_of_nums):
    """Returns a str with the numbers belonging to both input strs.
    If there is no number that belongs to both strs, it returns an empty str.
    The lists_of_nums parameter represents a sequence of two strs.
    Its first str represents a list of comma-separated numbers sorted in ascending order.
    Its second str represents another list of comma-separated numbers sorted in ascending order.
    Ex: ['2, 4, 11, 14, 30', '2, 4, 8, 11, 15, 21'] will return '2, 4, 11'
    """
    a, b = lists_of_nums
    a = {int(x) for x in a.split(',')}
    b = {int(x) for x in b.split(',')}

    res = sorted(a & b)

    res = (str(x) for x in res)
    return ', '.join(res)


if __name__ == '__main__':
    def check_test_some_cases():
        failed = 0
        TestCaseMapping = namedtuple(
            'test_case_mapping', ['input_val', 'expected'])
        test_cases = {
            1: TestCaseMapping(
                ['2, 4, 11, 14, 30', '2, 4, 8, 11, 15, 21'], '2, 4, 11'),
            2: TestCaseMapping(
                ['11, 23, 39, 410, 417, 418', '3, 11, 39, 410'], '11, 39, 410'),
            3: TestCaseMapping(
                ['3, 9, 12, 17, 20, 25, 51, 89', '4, 9, 12, 33, 51'
                 ], '9, 12, 51'),
            4: TestCaseMapping(
                ['4, 5, 6, 7, 8, 9', '10, 11, 12, 13, 14, 15'], ''),
            }
        for input_val, expected in test_cases.values():
            result = calc_intersection_of_strs_of_ordered_ints(input_val)
            failed += print_test_result(result, expected)
        print(f"{'-' * 25}\nTests FAILED: {failed}")

    check_test_some_cases()
