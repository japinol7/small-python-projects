from collections.abc import Iterable


def fizzbuzz(n: int) -> str:
    res = ''
    if n % 3 == 0 or '3' in str(n):
        res += 'Fizz'
    if n % 5 == 0 or '5' in str(n):
        res += 'Buzz'
    return res or str(n)


def fizzbuzz_range(n: int) -> Iterable:
    return (fizzbuzz(i) for i in range(1, n + 1))


def to_str(iterable: Iterable) -> str:
    return '\n'.join(iterable)
