"""Converts infix to prefix expression."""

from stack import Stack

OPERATOR_PRIORITY = {
    '^': 3,
    '*': 2,
    '/': 2,
    '+': 1,
    '-': 1,
    }
OPERATOR_PRIORITY_MIN = 0


def _get_operator_priority(operator):
    """Gets the priority of an operator."""
    return OPERATOR_PRIORITY.get(operator, OPERATOR_PRIORITY_MIN)


def _is_operator(char):
    """Checks if a character is an operator."""
    return not char.isalnum()


def convert_infix_to_postfix(expr):
    """Converts infix expression to postfix."""
    expr = '(' + expr + ')'
    expr_len = len(expr)
    stack = Stack()
    output = ''

    for i in range(expr_len):
        if expr[i].isalnum():
            output += expr[i]
            continue

        if expr[i] == '(':
            stack.push(expr[i])
            continue

        if expr[i] == ')':
            while stack.peek() != '(':
                output += stack.pop()
            stack.pop()
            continue

        if _is_operator(stack.peek()):
            if expr[i] == '^':
                while _get_operator_priority(expr[i]) <= _get_operator_priority(stack.peek()):
                    output += stack.pop()
            else:
                while _get_operator_priority(expr[i]) < _get_operator_priority(stack.peek()):
                    output += stack.pop()
            stack.push(expr[i])

    while stack:
        output += stack.pop()

    return output


def convert_infix_to_prefix(expr):
    """Converts infix expression to prefix."""
    expr = [ch for ch in expr[::-1] if not ch.isspace()]
    expr_len = len(expr)

    for i in range(expr_len):
        if expr[i] == '(':
            expr[i] = ')'
        elif expr[i] == ')':
            expr[i] = '('

    prefix = convert_infix_to_postfix(''.join(expr))
    prefix = prefix[::-1]
    return prefix.strip()


if __name__ == '__main__':
    s = "x+y*z/w+u"
    print(f"{s}")
    print(f"\t{convert_infix_to_prefix(s)}")

    s = "x+y-z"
    print(f"\n-----------\n{s}")
    print(f"\t{convert_infix_to_prefix(s)}")

    s = "x+y*z"
    print(f"\n-----------\n{s}")
    print(f"\t{convert_infix_to_prefix(s)}")
