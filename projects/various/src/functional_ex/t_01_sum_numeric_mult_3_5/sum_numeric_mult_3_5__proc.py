def sum_numeric_mult_3_5(limit: int) -> int:
    res = 0
    for n in range(1, limit):
        if n % 3 == 0 or n % 5 == 0:
            res += n
    return res


def main():
    for n in range(10, 51, 10):
        print(f"{n} -> {sum_numeric_mult_3_5(n)}")


if __name__ == '__main__':
    main()
