from collections.abc import Iterable


def array_to_phone_number(nums: Iterable) -> str:
    digits = (str(item) for item in nums)
    pattern = '({}{}{}) {}{}{}-{}{}{}{}'
    return pattern.format(*digits)
