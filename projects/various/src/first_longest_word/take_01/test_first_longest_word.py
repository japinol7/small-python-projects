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
    ("when beauty is the price, "
     "what mortal fears dying?", 'beauty'),
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
     "when the rivers freeze "
     "and summer ends.", 'snowflakes'),
    ("Beloved, gaze in thine own heart\n"
     "The holy tree is growing there;\n"
     "From joy the holy branches start,\n"
     "And all the trembling flowers they bear.\n"
     "Remembering all that shaken hair\n"
     "And how the winged sandals dart,\n"
     "Thine eyes grow full of tender care:\n"
     "Beloved, gaze in thine "
     "own heart.\n", 'Remembering'),
    ("If I can stop one heart from breaking,\n"
     "I shall not live in vain;\n"
     "If I can ease one life the aching,\n"
     "Or cool one pain,\n"
     "Or help one fainting robin\n"
     "Unto his nest again,\n"
     "I shall not live in vain.", 'breaking'),
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
     "How pure, how dear "
     "their dwelling-place.", 'dwelling-place'),
    ("As I was approaching Ovsyannikovo, "
     "I looked at the lovely sunset. "
     "A shaft of light in the piled-up clouds, and there, "
     "like a red irregular coal, the sun. "
     "All this above the forest, the rye. Joyful. "
     "And I thought to myself: No, this world is not a joke, "
     "not a vale of ordeal only and a passage to a better, "
     "eternal world, but one of the eternal worlds, "
     "which is good, joyful, and which we not only can, "
     "but must make finer and more joyful for those living with us, "
     "and for those who will live in it "
     "after us.", 'Ovsyannikovo'),
    ("To love is not to look at one another, "
     "but to look together in the same direction.", 'direction'),
    ("We have to keep the excitement like we did as children, "
     "but not their way; because theirs is the fruit of the ignorance, "
     "whereas the grown-up ones is the result "
     "of the wisdom.", 'excitement'),
    ("The essential quality of the human being is his freedom. "
     "The human being, by means of his intelligence, "
     "make himself aware of reality and he take charge of it. "
     "A man is what he does and his actions are dictated by his choices. "
     "To choice who we will be, that is the privilege "
     "and the risk of the human being.", 'intelligence'),
    ("What is needed is not the will to believe, "
     "but the wish to find out, "
     "which is the exact opposite.", 'opposite'),
    ("What makes the desert beautiful, "
     "is that somewhere it hides a well.", 'beautiful'),
    ("Your song is the embodiment of your dream. "
     "Make it of the finest things. "
     "It is the poetry in the way that you live. "
     "Not what you have, "
     "but what you do with what you have.", 'embodiment'),
    ("Baby it's a cold hard world out there\n"
     "Broken hearted people everywhere\n"
     "Takin' whatever love they get\n"
     "I don't wanna wind up like that, so\n\n"
     "Baby throw your arms around my neck\n"
     "Lay your pretty head against my chest\n"
     "Listen to one heartbeat then the next\n"
     "'Cause baby I don't wanna lose you yet", 'everywhere'),
    ("A need to transmit knowledge and skills, "
     "a desire to acquire them, "
     "are constants of the human condition. "
     "[...] "
     "There is no craft more privileged. "
     "To awaken in another human being powers, "
     "dreams beyond one's own; "
     "to induce in others a love for that which one loves; "
     "to make of one's inward present their future: "
     "this is a threefold adventure "
     "like no other.", 'privileged'),
    ("...Four good things had happened to her, in fact, "
     "since she came to Misselthwaite Manor. "
     "She had felt as if she had understood a robin "
     "and that he had understood her; "
     "she had run in the wind until her blood had grown warm; "
     "she had been healthily hungry for the first time in her life; "
     "and she had found out what it was to be sorry "
     "for some one..", 'Misselthwaite'),
    ("There are three different people in your life; "
     "they come into your life for a reason, "
     "for a season, or for a lifetime. ", 'different'),
    ("Your slightest look easily will unclose me "
     "though I have closed myself as fingers, "
     "you open always petal by petal myself "
     "as Spring opens (touching skilfully, mysteriously) "
     "her first rose "
     "(I do not know what it is about you "
     "that closes and opens; "
     "only something in me understands "
     "the voice of your eyes is deeper than all roses) "
     "nobody, not even the rain, "
     "has such small hands ", 'mysteriously'),
    ("[ironically] "
     "'You judge very properly' said Mr. Bennet, "
     "'and it is happy for you that you possess the talent "
     "of flattering with delicacy. "
     "May I ask whether these pleasing attentions "
     "proceed from the impulse of the moment, "
     "or are the result of previous study?", 'ironically'),
    ("She did not know it, but there with unborn futures "
     "reeled out of existence, rebellion flamed "
     "into coming centuries, "
     "people and underpeople died in strange causes, "
     "mothers changed the names of unborn lords "
     "and star-ships whispered back from places "
     "which men had not even imagined before. "
     "Space3, which had always been there, waiting "
     "for men’s notice, would come the sooner—because of her, "
     "because of the door, because of her next few steps, "
     "what she would say and the child she would meet. "
     "(The ballad-writers told the whole story later on, "
     "but they told it backwards, from their own knowledge "
     "of D’joan and what Elaine had done to set the worlds afire. "
     "The simple truth is the fact that a lonely woman "
     "went through a mysterious door. That is all. "
     "Everything else happened later.)", 'ballad-writers'),
    ("Good times come and they go,\n"
     "even a good man'll break\n"
     "He'll let his troubles bury him whole\n"
     "even though he knows what's at stake\n"
     "So I'm taking no chances, carrying over\n"
     "while I'm still good in His grace\n"
     "I'm no fool, mama, I know the difference\n"
     "between tempting and choosing my fate\n\n"
     "'cause Lord, I'm goin' uptown\n"
     "to the Harlem River to drown\n"
     "Dirty water is gonna cover me over\n"
     "and I'm not gonna make a sound", 'difference'),
    ("Charlie picks up the tree, smiles. "
     "Walks outside, stares at sky. \n"
     "Charlie (to himself): \n"
     "''Linus is right; "
     "I won't let all this commercialism ruin my Christmas. "
     "I'll take this little tree home, "
     "and I'll decorate it,"
     " and I\'ll show them it really will work in our play.''\n"
     "... Linus:\n"
     " ''I never thought it was such a bad little tree. "
     "It's not bad at all, really. "
     "Maybe it just needs a little love.''\n"
     "... Narrator: ''\n"
     "He looked at his little tree that no one had wanted, "
     "and he could hardly believe his eyes. "
     "His friends' efforts had transformed it "
     "into something truly special.", 'commercialism'),
    ("I wish I was in Carrighfergus,\n"
     "Only for nights in Bellygrant.\n"
     "I would swim over the deepest oceans,\n"
     "Only for nights in Bellygrant.\n", 'Carrighfergus'),
    ])
def test_get_first_longest_word(text, expected):
    assert get_first_longest_word(text) == expected
