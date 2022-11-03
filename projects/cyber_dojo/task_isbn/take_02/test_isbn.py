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
    ('978-0-262-13472-X', 'false'),
    ('978-13472-2', 'false'),
    ('978-0-A62-13472-1', 'false'),
    ])
def test_validate_isbn_13(input_isbn, expected):
    """Tests the validation of ISBN-13 codes."""
    result = validate_isbn(input_isbn)
    assert result == expected


@pytest.mark.parametrize('input_isbn, expected', [
    ('0471958697', 'true'),
    ('0 471 60695 2', 'true'),
    ('0-470-84525-2', 'true'),
    ('0-321-14653-0', 'true'),
    ('0-8044-2957-X', 'true'),
    ('0-9752298-0-X', 'true'),
    ('0-8044-2957-D', 'false'),
    ('0-470-84525-3', 'false'),
    ('0-4A0-84525-2', 'false'),
    ('0-470-*4525-2', 'false'),
    ('0-470-8425-2', 'false'),
    ])
def test_validate_isbn_10(input_isbn, expected):
    """Tests the validation of ISBN-10 codes."""
    result = validate_isbn(input_isbn)
    assert result == expected
