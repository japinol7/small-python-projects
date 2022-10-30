import pytest

from isbn import validate_isbn


@pytest.mark.parametrize('input_isbn, expected', [
    ('9780470059029', 'true'),
    ('978 0 471 48648 0', 'true'),
    ('978-0596809485', 'true'),
    ('978-0-13-149505-0', 'true'),
    ('978-0-262-13472-9', 'true'),
    ('978-0-262-13472-1', 'false'),
    ('978-0-262-13472-2', 'false'),
    ('978 0 A 471 48648 0', 'false'),
    ('978 0 * 471 48648 0', 'false'),
    ('978-13472-2', 'false'),
    ('978-0-A62-13472-1', 'false'),
    ])
def test_validate_isbn(input_isbn, expected):
    """Tests the validation of ISBN-13 codes."""
    result = validate_isbn(input_isbn)
    assert result == expected
