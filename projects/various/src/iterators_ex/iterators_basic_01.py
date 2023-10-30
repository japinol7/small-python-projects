from collections.abc import Iterable, Iterator, Generator


class NumRange:
    """Iterator class example."""

    def __init__(self, start: int, end: int, step: int = 1):
        self.value = start
        self.end = end
        self.step = step

        if self.step <= 0:
            raise ValueError("step must be greater than 0.")

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration

        current = self.value
        self.value += self.step
        return current


def num_range(start: int, end: int, step: int = 1):
    """Iterator as generator example."""
    if step <= 0:
        raise ValueError("step must be greater than 0.")

    while start < end:
        yield start
        start += step


def _print_isinstance(header=''):
    print(f"{header}\n"
          f"{isinstance(nums, Iterable)=}\n"
          f"{isinstance(nums, Iterator)=}\n"
          f"{isinstance(nums, Generator)=}")


if __name__ == '__main__':
    nums = NumRange(1, 10, 2)
    _print_isinstance("Iterator class example")
    for num in nums:
        print(num)

    print('\n---------')

    nums = num_range(1, 10, 2)
    _print_isinstance("Iterator class example")
    for num in nums:
        print(num)
