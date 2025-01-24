CHARS_TO_EXCLUDE_LEFT = {
        '\\', '/', 
        }
WORDS_TO_KEEP = 'tests', 'test', 'spec', 'step'
SEPARATORS = '-', '_', '.'


def _keep_word_on_the_right(text, word_to_keep, left_mark, right_mark):
    word_to_keep_idx = text.find(word_to_keep)
    if word_to_keep_idx != -1:
        if 0 < word_to_keep_idx < right_mark:
            right_mark = word_to_keep_idx
            if text[right_mark - 1] in SEPARATORS:
                right_mark -= 1
            right_mark += left_mark

    return right_mark


def _keep_word_on_the_left(text, word_to_keep, left_mark):
    word_to_keep_idx = text.find(word_to_keep)
    if word_to_keep_idx != -1:  
        if word_to_keep_idx >= left_mark:
            left_mark = word_to_keep_idx + len(word_to_keep)
            if text[left_mark] in SEPARATORS:
                left_mark += 1

    return left_mark


def filename_range(filename):
    if not filename:
        return []

    name = filename.lower()

    # Remove chars from the left to the last char to exclude
    left_mark = 0
    for i, ch in enumerate(name[::-1]):
        if ch in CHARS_TO_EXCLUDE_LEFT:
            left_mark = len(name) - i
            break

    # Remove chars from the right of the first dot char
    right_mark = len(name)
    for i, ch in enumerate(name):
        if ch == '.':
            right_mark = i
            break

    # Remove words to keep on the right and their separators
    name_tp = name[left_mark:]
    for word in WORDS_TO_KEEP:
        right_mark = _keep_word_on_the_right(
                name_tp, word, left_mark, right_mark)

    # Remove words to keep on the left and their separators
    name_tp = name[:right_mark]
    for word in WORDS_TO_KEEP:
        left_mark = _keep_word_on_the_left(name_tp, word, left_mark)

    return [left_mark, right_mark]


if __name__ == '__main__':
    filename = 'wibble/test/hiker_spec.rb'
    name_range = filename_range(filename)
    print(filename, ' -> ', name_range, ' -> ', filename[name_range[0]:name_range[1]])
