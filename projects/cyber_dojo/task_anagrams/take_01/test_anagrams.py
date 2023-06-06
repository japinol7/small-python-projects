import pytest

from anagrams import Anagrams

ANAGRAMS_FOR_BIRO = [
    'bior', 'biro', 'boir', 'bori', 'brio', 'broi',
    'ibor', 'ibro', 'iobr', 'iorb', 'irbo', 'irob',
    'obir', 'obri', 'oibr', 'oirb', 'orbi', 'orib',
    'rbio', 'rboi', 'ribo', 'riob', 'robi', 'roib',
    ]


class TestAnagrams:
    @pytest.mark.parametrize('text, expected', [
        ('', []),
        ('a', ['a']),
        ('ab', ['ab', 'ba']),
        ('biro', ANAGRAMS_FOR_BIRO),
        ])
    def test_generate_anagrams(self, text, expected):
        result = Anagrams.generate(text)
        result = sorted(list(result))
        assert result == expected
