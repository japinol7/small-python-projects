def array_to_phone_number(n):
    digits = (str(item) for item in n)
    pattern = '({}{}{}) {}{}{}-{}{}{}{}'
    return pattern.format(*digits)
