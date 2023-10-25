from typing import Iterable


def fizzbuzz(num: int) -> str:
    res = ''
    if num % 3 == 0 or '3' in str(num):
        res += 'Fizz'
    if num % 5 == 0 or '5' in str(num):
        res += 'Buzz'
    return res or str(num)


def fizzbuzz_range(num: int) -> Iterable:
    return (fizzbuzz(x) for x in range(1, num + 1))


def to_str(iterable: Iterable) -> str:
    return '\n'.join((str(x) for x in iterable))
