TOTAL_BUCKETS = 10


class NaiveDict:
    def __init__(self):
        self.key_arr = [[] for _ in range(TOTAL_BUCKETS)]
        self.values_arr = [[] for _ in range(TOTAL_BUCKETS)]

    def __setitem__(self, key, value):
        idx = hash(key) % TOTAL_BUCKETS
        self.key_arr[idx].append(key)
        self.values_arr[idx].append(value)

    def __getitem__(self, key):
        idx = hash(key) % TOTAL_BUCKETS
        try:
            j = self.key_arr[idx].index(key)
        except ValueError:
            raise KeyError(key)
        return self.values_arr[idx][j]

    def __iter__(self):
        return iter([x for items in self.key_arr for x in items])

    def __str__(self):
        return '\n'.join(
            [str(x) for items in self.key_arr for x in items]
        )

    def values(self):
        return iter([x for items in self.values_arr for x in items])

    def all_buckets(self):
        return (item for item in self.key_arr)


def _main():
    dict_1 = NaiveDict()
    dict_1['Ritchie Blackmore'] = 'guitar'
    dict_1['Hilary Hahn'] = 'violin'
    dict_1['Wynton Marsalis'] = 'trumpet'

    print("\nAll buckets:")
    for k in dict_1.all_buckets():
        print(k)

    print(f"\n{dict_1['Hilary Hahn']=}")

    print(f"\nItems:\n{dict_1}")

    print("\nItems:")
    for k, v in zip(dict_1, dict_1.values()):
        print(f"{k}: {v}")


if __name__ == '__main__':
    _main()
