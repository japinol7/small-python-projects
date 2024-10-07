def check_matching_brackets(text):
    """It considers these bracket marks: '(', '{', '['."""
    open_marks = tuple('({[')
    close_marks = tuple(')}]')
    marks_map = dict(zip(open_marks, close_marks))
    stack = []

    for ch in text:
        if ch in open_marks:
            stack.append(marks_map[ch])
            continue
        if ch in close_marks:
            if not stack or ch != stack.pop():
                return False
    if not stack:
        return True
    return False
