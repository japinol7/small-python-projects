import math


class FilenameRange:
    @staticmethod
    def find_min_pos_of_strs(str_, strs):
        res = math.inf
        for sub_str in strs:
            mark = str_.find(sub_str)
            if mark != -1 and mark - 1 < res:
                res = mark - 1
        return res

    @staticmethod
    def find_max_starting_pos_of_strs(str_, strs):
        res = -math.inf
        for sub_str in strs:
            mark = str_.find(sub_str)
            if mark == 0 and len(sub_str)> res:
                res = len(sub_str)
        return res

    @staticmethod
    def find_min_right_starting_pos_of_strs(str_, strs):
        res = math.inf
        for sub_str in strs:
            mark = str_.rfind(sub_str)
            if mark != -1 and mark < res:
                res = mark
        return res

    @staticmethod
    def filename_range(filename):
        if not filename:
            return []

        name = filename.lower()
        # Find left mark of the name if starts with a starting string
        left_mark = max(0,
                        FilenameRange.find_max_starting_pos_of_strs(name, [
                            'test', 'test_', 'test-', 'test.',
                            'tests', 'tests_', 'tests-', 'tests.',
                        ]))

        # Find left mark of the name considering that must start after a directory char if there is at least one
        mark = FilenameRange.find_min_right_starting_pos_of_strs(name, ['/', '\\'])
        if mark > 0 and mark != math.inf and mark + 1 > left_mark:
            left_mark = mark + 1

        # Find right mark of the name if discarding ending strings that start with a test string
        right_mark = len(name) - 1
        right_mark = min(right_mark,
                         FilenameRange.find_min_pos_of_strs(name[left_mark:], [
                             '.',
                             'test', 'spec', 'step',
                             '_test', '_spec', '_step',
                             '-test', '-spec', '-step',
                         ])) + left_mark

        if left_mark >= right_mark:
            left_mark = 0

        return [left_mark, right_mark + 1]
