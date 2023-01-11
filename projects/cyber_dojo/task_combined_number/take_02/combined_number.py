class CombinedNumber:
    @staticmethod
    def combined_number(nums):
        if not nums:
            return ''

        res = [str(x) for x in nums]

        # Sort items using the bubblesort algorithm
        res_len = len(res)
        some_swap = False
        for i in range(res_len - 1):
            for j in range(0, res_len - i - 1):
                if res[j] + res[j + 1] < res[j + 1] + res[j]:
                    res[j], res[j + 1] = res[j + 1], res[j]
                    some_swap = True
            if not some_swap:
                break

        return ''.join(res)
