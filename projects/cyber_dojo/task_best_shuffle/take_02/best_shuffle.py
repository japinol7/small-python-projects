import random


class BestShuffle:

    @staticmethod
    def _calc_ranking(original, candidate):
        return sum(1 if x == y else 0 for x, y in zip(original, candidate))

    def best_shuffle(self, input_val):
        if not input_val:
            return ''
        candidate = list(input_val)
        input_len = len(input_val)
        groups = list(range(input_len)), list(range(input_len))
        for group in groups:
            random.shuffle(group)

        range_i, range_j = groups
        for i in range_i:
            for j in range_j:
                if all((i != j,
                        candidate[j] != candidate[i],
                        input_val[i] != candidate[j],
                        input_val[j] != candidate[i],
                        )):
                    candidate[j], candidate[i] = candidate[i], candidate[j]
                    break
        candidate = ''.join(candidate)
        return f"{input_val}, {candidate}, ({self._calc_ranking(input_val, candidate)})"
