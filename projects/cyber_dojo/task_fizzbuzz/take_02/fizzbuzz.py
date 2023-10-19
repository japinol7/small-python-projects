def fizzbuzz(num):
    res = ''
    if num % 3 == 0:
        res += 'Fizz'
    if num % 5 == 0:
        res += 'Buzz'
    return res or str(num)


def fizzbuzz_range(num):
    return (fizzbuzz(x) for x in range(1, num + 1))


def to_str(iterable):
    return '\n'.join((str(x) for x in iterable))
