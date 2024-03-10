from collections.abc import Sequence, Callable


def sum_recursive(seq: Sequence[int]) -> int:
    if len(seq) == 0:
        return 0
    return seq[0] + sum_recursive(seq[1:])


def until(limit: int,
          filter_func: Callable[[int], bool],
          val: int
          ) -> list[int]:
    if val == limit:
        return []
    elif filter_func(val):
        return [val] + until(limit, filter_func, val + 1)
    else:
        return until(limit, filter_func, val + 1)


def sum_numeric_mult_3_5(limit: int) -> int:
    return sum_recursive(until(
        limit,
        filter_func=lambda n: n % 3 == 0 or n % 5 == 0,
        val=0))


def main():
    for n in range(10, 51, 10):
        print(f"{n} -> {sum_numeric_mult_3_5(n)}")


if __name__ == '__main__':
    main()
