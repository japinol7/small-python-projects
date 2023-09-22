import pytest

from convert_infix_to_prefix import convert_infix_to_prefix


@pytest.mark.parametrize('input_expr, expected', [
    ('', ''),
    ('x+y*z/w+u', '++x/*yzwu'),
    ('x+y-z', '-+xyz'),
    ('x+5-y', '-+x5y'),
    ('x+y*z', '+x*yz'),
    ('(x+a)/b', '/+xab'),
    ('(x+5)/7', '/+x57'),
    ('x*(y-z)', '*x-yz'),
    ('w*(x-y)/z', '/*w-xyz'),
    ('x|y|z', '||xyz'),
    ('x|(y&z)', '|x&yz'),
    ('w*x|y*z', '|*wx*yz'),
    ('w*x+1|y*z+a', '|+*wx1+*yza'),
    ('x + y - z', '-+xyz'),
    ('x + 5 - y', '-+x5y'),
    ('(x + a) / b', '/+xab'),
    ])
def test_validate_isbn(input_expr, expected):
    result = convert_infix_to_prefix(input_expr)
    assert result == expected
