OPEN_MARKS = '(', '{', '['
CLOSE_MARKS = ')', '}', ']'


def are_parentheses_balanced(str_):
    marks_map = dict(zip(OPEN_MARKS, CLOSE_MARKS))
    stack = []

    for ch in str_:
        if ch in OPEN_MARKS:
            stack.append(marks_map[ch])
            continue
        if ch in CLOSE_MARKS:
            if not stack or ch != stack.pop():
                return False
    if not stack:
        return True
    return False
