def check_matching_brackets(text):
    mark_count = 0
    for ch in text:
        if ch == '(':
            mark_count += 1
        elif ch == ')':
            mark_count -= 1
        if mark_count < 0:
            return False
    return False if mark_count else 1
