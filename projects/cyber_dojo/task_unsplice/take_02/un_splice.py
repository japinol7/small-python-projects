import re


def un_splice(text):
    return re.sub(r'\\\n', '', text)
