from stack import Stack


class HanoiTowers:
    """The Towers of Hanoi."""

    def __init__(self, n_discs):
        self.n_discs = n_discs
        self.tower_start = None
        self.tower_tmp = None
        self.tower_end = None

        self.reset()

    def reset(self):
        self.tower_start = Stack()
        self.tower_tmp = Stack()
        self.tower_end = Stack()

        for disc in range(1, self.n_discs + 1):
            self.tower_start.push(disc)

    def __str__(self):
        return "HanoiTowers\n" \
               f"\tn_discs: {self.n_discs}\n" \
               f"\ttower_start: {self.tower_start}\n" \
               f"\ttower_tmp: {self.tower_tmp}\n" \
               f"\ttower_end: {self.tower_end}"

    def move_discs_to_end_tower(self, start=None, end=None, tmp=None, disc=None):
        start = start or self.tower_start
        end = end or self.tower_end
        tmp = tmp or self.tower_tmp
        disc = disc or self.n_discs

        if disc == 1:
            end.push(start.pop())
            return

        self.move_discs_to_end_tower(start, tmp, end, disc - 1)
        self.move_discs_to_end_tower(start, end, tmp, 1)
        self.move_discs_to_end_tower(tmp, end, start, disc - 1)


def main():
    hanoi_towers = HanoiTowers(5)
    print(f"\nInitial state:\n{hanoi_towers}")

    hanoi_towers.move_discs_to_end_tower()
    print(f"\nAfter processing:\n{hanoi_towers}")


if __name__ == "__main__":
    main()
