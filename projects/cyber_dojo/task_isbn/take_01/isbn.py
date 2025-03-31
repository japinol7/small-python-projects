def validate_isbn(isbn):
    """Validates if a given string is a valid ISBN-13 code."""
    if any(not ch.isnumeric() and ch != '-' and ch != ' ' for ch in isbn):
        return 'false'

    isbn = [int(ch) for ch in isbn if ch.isnumeric()]
    if len(isbn) != 13:
        return 'false'

    # Multiply each digit alternately by 1 or 3 and sum these products together
    check_digit = sum(
        x * 3 if i % 2 == 0 else x for i, x in enumerate(isbn[:-1], start=1)
        )
    check_digit %= 10
    check_digit = (10 - check_digit) % 10

    if check_digit != isbn[-1]:
        return 'false'

    return 'true'
