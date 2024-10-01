def count_factors(n: int) -> int:
    factor_count = 0
    num = 1
    while num * num < n:
        if n % num == 0:
            factor_count += 2
        num += 1
    if num * num == n:
        factor_count += 1
    return factor_count
