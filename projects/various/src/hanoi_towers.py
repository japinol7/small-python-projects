from tools.logger import logger
from tools.logger.logger import log
from stack import Stack

MIN_DISCS = 1
MAX_DISCS = 24


class HanoiTowersException(Exception):
    pass


class HanoiTowers:
    """The Towers of Hanoi. This solver uses a recursive approach."""

    def __init__(self, n_discs):
        self.n_discs = n_discs
        self.tower_start = None
        self.tower_tmp = None
        self.tower_end = None

        if not (MIN_DISCS <= n_discs <= MAX_DISCS):
            raise HanoiTowersException(f"User Error. Invalid number of discs: "
                                       f"must be between {MIN_DISCS} and {MAX_DISCS} .")

        self._setup()

    def _setup(self):
        self.tower_start = Stack()
        self.tower_tmp = Stack()
        self.tower_end = Stack()

        for disc in range(1, self.n_discs + 1):
            self.tower_start.push(disc)

    def __str__(self):
        return f"HanoiTowers for n_discs: {self.n_discs}\n" \
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
    logger.add_stdout_handler()
    log.info("Start HanoiTowers")

    hanoi_towers = HanoiTowers(15)
    log.info(f"Initial state:\n{hanoi_towers}")

    hanoi_towers.move_discs_to_end_tower()
    log.info(f"State after processing:\n{hanoi_towers}")


if __name__ == "__main__":
    main()
