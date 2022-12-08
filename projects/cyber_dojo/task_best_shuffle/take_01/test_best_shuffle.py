import pytest

from best_shuffle import BestShuffle


class TestBestShuffle:
    @pytest.mark.parametrize('input_val, expected', [
        ("tree", "tree, eert, (0)"),
        ("abracadabra", "abracadabra, baabacadrar, (0)"),
        ("seesaw", "seesaw, assewe, (0)"),
        ("elk", "elk, kel, (0)"),
        ("grrrrrr", "grrrrrr, rgrrrrr, (5)"),
        ("up", "up, pu, (0)"),
        ("a", "a, a, (1)"),
        ("mediate", "mediate, adeeimt, (0)"),
        ("", "")
        ])
    def test_best_shuffle(self, input_val, expected):
        result = BestShuffle().best_shuffle(input_val, to_sort=True)
        assert result == expected
