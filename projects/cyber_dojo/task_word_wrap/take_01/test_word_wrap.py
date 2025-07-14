from word_wrap import word_wrap
from conftest import TEST_INPUT_01_WIDTH_TWENTY


def test_word_wrap_empty_string():
    text, max_width = '', 10
    expected = ''
    result = word_wrap(text, max_width)
    assert result == expected


def test_word_wrap_one_word_enough_space():
    text, max_width = 'Hello', 10
    expected = 'Hello'
    result = word_wrap(text, max_width)
    assert result == expected


def test_word_wrap_one_word_not_enough_space():
    text, max_width ='Hellow-beautiful', 10
    expected = 'Hellow-bea\nutiful'
    result = word_wrap(text, max_width)
    assert result == expected


def test_word_wrap_two_words_not_enough_space():
    text, max_width = 'Hello world', 10
    expected = 'Hello\nworld'
    result = word_wrap(text, max_width)
    assert result == expected


def test_word_wrap_input_01_width_twenty():
    text, max_width, expected = TEST_INPUT_01_WIDTH_TWENTY
    result = word_wrap(text, max_width)
    assert result == expected
