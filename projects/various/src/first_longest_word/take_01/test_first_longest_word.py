import pytest

from first_longest_word import get_first_longest_word


@pytest.mark.parametrize("text, expected", [
    ("", ''),
    (" ", ''),
    ("&!=", ''),
    ("Have a nice time!", 'Have'),
    ("Have a&!! nice weekend", 'weekend'),
    ("Are you self-aware?", 'self-aware'),
    ("I really like AnomGirl91", 'AnomGirl91'),
    ("when beauty is the price, what mortal fears dying?", 'beauty'),
    ("Upon a darkened night\n"
     "the flame of love was burning in my breast\n"
     "And by a lantern bright\n"
     "I fled my house while all in quiet rest\n"
     "Shrouded by the night\n"
     "and by the secret stair I quickly fled\n"
     "The veil concealed my eyes\n"
     "while all within lay quiet as the dead.\n\n"
     "[...]\n\n"
     "That fire was led me on\n"
     "without a guide or light\n"
     "than that which burned\n"
     "so deeply in my heart\n", 'concealed'),
    ("The Holy Grail held the pawns while "
     "kings and bishops bow to grace", 'bishops'),
    ("Walking through the leaves, falling from the trees\n"
     "feeling like a stranger nobody sees.\n"
     "So many things we never will undo.\n"
     "I know you’re sorry, I’m sorry, too.", 'stranger'),
    ("Cascading stars on the slumbering hills\n"
     "They are dancing as far as the sea\n"
     "Riding o'er land, you can feel its gentle hand\n"
     "Leading on to its destiny", 'slumbering'),
    ("Love should be a simple blend\n"
     "A whispering on the shore\n"
     "No clever words you can't defend\n"
     "They lead to never more.", 'whispering'),
    ("If you go when the snowflakes storm,\n"
     "when the rivers freeze and summer ends.", 'snowflakes'),
    ("Beloved, gaze in thine own heart\n"
    "The holy tree is growing there;\n"
    "From joy the holy branches start,\n"
    "And all the trembling flowers they bear.\n"
    "Remembering all that shaken hair\n"
    "And how the winged sandals dart,\n"
    "Thine eyes grow full of tender care:\n"
    "Beloved, gaze in thine own heart.\n", 'Remembering'),
    ("She walks in beauty, like the night\n"
    "Of cloudless climes and starry skies;\n"
    "And all that’s best of dark and bright\n"
    "Meet in her aspect and her eyes;\n"
    "Thus mellowed to that tender light\n"
    "Which heaven to gaudy day denies.\n\n"
    "One shade the more, one ray the less,\n"
    "Had half impaired the nameless grace\n"
    "Which waves in every raven tress,\n"
    "Or softly lightens o’er her face;\n"
    "Where thoughts serenely sweet express,\n"
    "How pure, how dear their dwelling-place.", 'dwelling-place'),
    ("Baby it's a cold hard world out there\n"
    "Broken hearted people everywhere\n"
    "Takin' whatever love they get\n"
    "I don't wanna wind up like that, so\n\n"
    "Baby throw your arms around my neck\n"
    "Lay your pretty head against my chest\n"
    "Listen to one heartbeat then the next\n"
    "'Cause baby I don't wanna lose you yet", 'everywhere'),
    ("I wish I was in Carrighfergus,\n"
    "Only for nights in Bellygrant.\n"
    "I would swim over the deepest oceans,\n"
    "Only for nights in Bellygrant.\n", 'Carrighfergus'),
    ])
def test_get_first_longest_word(text, expected):
    assert get_first_longest_word(text) == expected
