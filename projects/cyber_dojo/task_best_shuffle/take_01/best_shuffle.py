from itertools import permutations


class BestShuffle:
    @staticmethod
    def _calc_ranking(original, candidate):
        return sum(1 if x == y else 0 for x, y in zip(original, candidate))

    def best_shuffle(self, input_val, to_sort=False):
        # TODO: Very inefficient version. Must improve performance.
        if not input_val:
            return ''
        original = list(input_val)
        candidates = set(permutations(original))
        if to_sort:
            candidates = sorted(candidates)
        ranking = {}
        for candidate in candidates:
            ranking[''.join(candidate)] = self._calc_ranking(original, candidate)

        best_candidate = min(ranking.items(), key=lambda x: x[1])
        return f"{input_val}, {best_candidate[0]}, ({best_candidate[1]})"
