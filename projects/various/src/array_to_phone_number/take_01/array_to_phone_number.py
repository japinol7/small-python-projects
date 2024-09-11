from collections.abc import Iterable


def array_to_phone_number(nums: Iterable) -> str:
    return '({}{}{}) {}{}{}-{}{}{}{}'.format(*nums)
