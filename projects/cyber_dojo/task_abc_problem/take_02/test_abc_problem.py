import pytest

from abc_problem import ABCProblem


class TestABCProblem:
    @pytest.mark.parametrize('word, expected', [
        ('A', True),
        ('BARK', True),
        ('BOOK', False),
        ('TREAT', True),
        ('COMMON', False),
        ('squad', True),
        ('CONFUSE', True),
        ('ConFUSE', True),
        ('', False),
        ])
    def test_can_make_word(self, word, expected):
        result = ABCProblem.can_make_word(word)
        assert result == expected
