DECIMALS = 6


class CalcStats:
    def __init__(self, nums):
        self.nums = nums

    def max(self):
        return max(self.nums)

    def min(self):
        return min(self.nums)

    def len(self):
        return len(self.nums)

    def average(self):
        return round(sum(self.nums) / len(self.nums), 6)

    @staticmethod
    def to_str(statistics_nums):
        return f"min: {statistics_nums[0]},\n" \
               f"max: {statistics_nums[1]},\n" \
               f"count: {statistics_nums[2]},\n" \
               f"average: {statistics_nums[3]}"

    def calculate(self):
        if not self.nums:
            return []

        return [
            self.min(),
            self.max(),
            self.len(),
            self.average(),
            ]
