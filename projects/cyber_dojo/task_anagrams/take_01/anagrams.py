from itertools import permutations


class Anagrams:

    @staticmethod
    def generate(text):
        if not text:
            return []

        yield from (''.join(x) for x in permutations(text, len(text)))
