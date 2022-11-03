def _validate_isbn_13(isbn_digits, isbn_dc):
    """Helper that validates if a given string is a valid ISBN-13 code."""
    if not isbn_dc.isnumeric():
        return 'false'

    isbn_dc = int(isbn_dc)
    # Multiply each digit alternately by 1 or 3 and sum these products together
    check_digit = sum((
            x * 3 if i % 2 == 0 else x for i, x in enumerate(isbn_digits, start=1)
        ))
    check_digit %= 10
    check_digit = (10 - check_digit) % 10

    if check_digit != isbn_dc:
        return 'false'
    return 'true'


def _validate_isbn_10(isbn_digits, isbn_dc):
    """Validates if a given string is a valid ISBN-10 code."""
    if not isbn_dc.isnumeric() and isbn_dc != 'X':
        return 'false'

    if isbn_dc != 'X':
        isbn_dc = int(isbn_dc)

    # Multiply each digit by its position number and sum these products together
    check_digit = sum((
            x * i for i, x in enumerate(isbn_digits, start=1)
        ))
    check_digit %= 11
    if check_digit == 10:
        check_digit = 'X'

    if check_digit != isbn_dc:
        return 'false'
    return 'true'


def validate_isbn(isbn):
    """Validates if a given string is a valid ISBN-13 or a valid ISBN-10 code."""
    if any(not ch.isnumeric() and ch != '-' and ch != ' ' for ch in isbn[:-1]):
        return 'false'

    isbn_nums_without_dc = [int(ch) for ch in isbn[:-1] if ch.isnumeric()]
    isbn_len = len(isbn_nums_without_dc) + 1

    if isbn_len == 13:
        return _validate_isbn_13(isbn_nums_without_dc, isbn[-1])
    if isbn_len == 10:
        return _validate_isbn_10(isbn_nums_without_dc, isbn[-1])
    return 'false'
