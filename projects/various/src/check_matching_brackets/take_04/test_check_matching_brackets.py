import pytest

from check_matching_brackets import check_matching_brackets


@pytest.mark.parametrize("input_text, expected", [
    ("Hi", True),
    ("(hello)(buddy))", False),
    ("(h(ello)) b(uddy)", True),
    ("(hello)) (world) (b(uddy)", False),
    ("[h(ello)] b(uddy)", True),
    ("[h(ello)] b{uddy}", True),
    ("[hello]{budd(y)}", True),
    ("[hello]{budd(y})", False),
    ("[hello](buddy))", False),
    ("[hello]{budd)y(}", False),
    ])
def test_check_matching_brackets(input_text, expected):
    assert check_matching_brackets(input_text) == expected
