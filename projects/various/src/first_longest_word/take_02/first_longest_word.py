import re


def get_first_longest_word(str_: str) -> str:
    pattern = re.compile(r'[^a-zA-Z1-9-]+')
    x = pattern.split(str_,)
    return max(x, key=len)
