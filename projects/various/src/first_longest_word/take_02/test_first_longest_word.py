import pytest

from first_longest_word import get_first_longest_word


@pytest.mark.parametrize("text, expected", [
    ("", ''),
    (" ", ''),
    ("&!=", ''),
    ("Have a nice time!", 'Have'),
    ("Have a&!! nice weekend", 'weekend'),
    ("I really like AnomGirl91", 'AnomGirl91'),
    ("when beauty is the price, what mortal fears dying?", 'beauty'),
    ("That fire was led me on\nwithout a guide or light\n"
     "than that which burned\nso deeply in my heart", 'without'),
    ("The Holy Grail held the pawns while "
     "kings and bishops bow to grace", 'bishops'),
    ("Walking through the leaves, falling from the trees\n"
     "feeling like a stranger nobody sees.\n"
     "So many things we never will undo.\n"
     "I know you’re sorry, I’m sorry, too.", 'stranger'),
    ("If you go when the snowflakes storm, "
     "when the rivers freeze and summer ends.", 'snowflakes'),
    ])
def test_get_first_longest_word(text, expected):
    assert get_first_longest_word(text) == expected
