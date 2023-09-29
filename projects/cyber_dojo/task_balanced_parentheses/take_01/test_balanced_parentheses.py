import pytest

from balanced_parentheses import are_parentheses_balanced


@pytest.mark.parametrize('input_val, expected', [
    ('', True),
    ('()', True),
    ('{}', True),
    ('{()}', True),
    ('{[()]}', True),
    ('[({})]', True),
    ('{}([])', True),
    ('{()}[[{}]]', True),
    ('[]]', False),
    ('{{)(}}', False),
    ('({)}', False),
    ])
def test_balanced_parentheses(input_val, expected):
    assert are_parentheses_balanced(input_val) is expected
