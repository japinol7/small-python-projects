from bubblesort import bubblesort_with_compare


class CombinedNumber:
    @staticmethod
    def combined_number(nums):
        if not nums:
            return ''

        res = [str(x) for x in nums]
        bubblesort_with_compare(res, compare_func=lambda x, y: x + y < y + x)
        return ''.join(res)
