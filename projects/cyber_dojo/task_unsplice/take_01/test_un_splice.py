import pytest

from un_splice import un_splice


@pytest.mark.parametrize('value, expected', [
    ('', ''),
    ('ab\\\ncd\\\nef', 'abcdef'),
    ('abc\\\ndef', 'abcdef'),
    ('abc\n\\def', 'abc\n\\def'),
    ('abc\\def', 'abc\\def'),
    ('abc\ndef', 'abc\ndef'),
    ('abcdef', 'abcdef'),
    ])
def test_un_splice(value, expected):
    assert un_splice(value) == expected
