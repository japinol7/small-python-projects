def get_first_longest_word(str_: str) -> str:
    words = ''.join(
        ch for ch in str_ if ch.isalnum() or ch.isspace() or ch in {'-', '·'}
    ).split()
    return max(words, key=len) if words else ''
