from collections.abc import Generator

def calculate_factors(n: int) -> Generator[int, None, None]:
    for num in range(1, n + 1):
        if n % num == 0:
            yield num
