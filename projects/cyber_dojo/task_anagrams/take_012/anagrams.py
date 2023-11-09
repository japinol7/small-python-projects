from itertools import permutations


def generate_anagrams(text):
    if not text:
        return []

    yield from (''.join(x) for x in permutations(text, len(text)))
