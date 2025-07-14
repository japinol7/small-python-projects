def word_wrap(text, max_width):
    res = text

    if len(res) > max_width:
        res = (res[:max_width] + '\n' +
               word_wrap(res[max_width:], max_width))

    return res
