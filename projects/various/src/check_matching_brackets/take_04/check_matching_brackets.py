def check_matching_brackets(text):
    """It considers these bracket marks: '(', '{', '['."""
    open_marks = ["[", "{", "("]
    close_marks = ["]", "}", ")"]
    stack = []
    for i in text:
        if i in open_marks:
            stack.append(i)
        elif i in close_marks:
            pos = close_marks.index(i)
            if ((len(stack) > 0) and
                    (open_marks[pos] == stack[len(stack) - 1])):
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    return False
