class CombinedNumber:
    @staticmethod
    def combined_number(nums):
        if not nums:
            return ''

        res = [str(x) for x in nums]

        # Sort items
        res_len = len(res)
        for i in range(res_len):
            for j in range(res_len):
                if res[i] + res[j] > res[j] + res[i]:
                    res[i], res[j] = res[j], res[i]

        return ''.join(res)
