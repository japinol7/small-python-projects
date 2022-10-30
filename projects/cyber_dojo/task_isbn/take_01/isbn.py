def validate_isbn(isbn):
    """Validates if a given string is a valid ISBN-13 code."""
    isbn_nums = [int(ch) for ch in isbn if ch.isnumeric()]
    isbn_digits = isbn_nums[:-1]
    isbn_control_digit_input = isbn_nums[-1]
    if len(isbn_nums) != 13:
        return 'false'

    # Multiply each digit alternately by 1 or 3 and sum these products together
    check_digit = sum((
            x * 3 if i % 2 == 0 else x for i, x in enumerate(isbn_digits, start=1)
        ))
    check_digit %= 10
    check_digit = (10 - check_digit) % 10

    if check_digit != isbn_control_digit_input:
        return 'false'
    return 'true'
