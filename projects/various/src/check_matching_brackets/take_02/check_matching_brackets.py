def check_matching_brackets(text):
    left_mark = text.rfind('(')
    right_mark = text.find(')', left_mark)
    new_string = text[:left_mark] + text[right_mark + 1:]

    if 0 < new_string.count('(') is new_string.count(')') > 0:
        return check_matching_brackets(new_string)
    if new_string.count('(') != new_string.count(')'):
        return False
    return True
