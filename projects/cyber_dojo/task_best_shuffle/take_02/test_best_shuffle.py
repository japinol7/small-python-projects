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
        ("immediately", "immediately, adeielimmyt, (0)"),
        ("thegreatestbearofalltime", "thegreatestbearofalltime, harttgmerbaeleofleeiastt, (0)"),
        ("you must be kidding; right; buddy?",
         "you must be kidding; right; buddy?, ui?byiyrd tgt mue;d uhd;oi gkd bns, (0)"),
        ])
    def test_best_shuffle(self, input_val, expected):
        """Test only if the original string and the score are correct.
        For the shuffled string only tests its length and if all the letters are there.
        """
        result = BestShuffle().best_shuffle(input_val)
        result_split = result.split(', ')
        expected_split = expected.split(', ')
        assert result_split[0] == expected_split[0]
        assert result_split[2] == expected_split[2]
        assert len(result_split[1]) == len(expected_split[1])
        assert sorted(result_split[1]) == sorted(expected_split[1])

    def test_best_shuffle_empty_str(self):
        input_val = ''
        result = BestShuffle().best_shuffle(input_val)
        expected = ''
        assert result == expected
