from tools.logger import logger
from tools.logger.logger import log
from stack import Stack

MIN_DISCS = 1
MAX_DISCS = 24


class HanoiTowersException(Exception):
    pass


class HanoiTowers:
    """The Towers of Hanoi. This solver uses a recursive approach."""

    def __init__(self, n_discs, to_log_moves=False):
        self.n_discs = n_discs
        self.to_log_moves = to_log_moves
        self.tower_start = None
        self.tower_tmp = None
        self.tower_end = None
        self.move = 1

        if not (MIN_DISCS <= n_discs <= MAX_DISCS):
            raise HanoiTowersException(f"User Error. Invalid number of discs: "
                                       f"must be between {MIN_DISCS} and {MAX_DISCS} .")

        self._setup()

    def _setup(self):
        self.tower_start = Stack(name='tower_start')
        self.tower_tmp = Stack(name='tower_tmp')
        self.tower_end = Stack(name='tower_end')

        for disc in range(self.n_discs, 0, -1):
            self.tower_start.push(disc)

    def __str__(self):
        return f"HanoiTowers for n_discs: {self.n_discs}\n" \
               f"\ttower_start: {self.tower_start}\n" \
               f"\ttower_tmp: {self.tower_tmp}\n" \
               f"\ttower_end: {self.tower_end}"

    def move_disc_between_towers(self, start, end, tmp, disc):
        if disc == 1:
            self.to_log_moves and log.info(f"{self.move:2}. Move disc {start.peek()} from {start.name} to {end.name}")
            self.move += 1
            end.push(start.pop())
            return

        self.move_disc_between_towers(start, tmp, end, disc - 1)
        self.move_disc_between_towers(start, end, tmp, 1)
        self.move_disc_between_towers(tmp, end, start, disc - 1)

    def move_discs_to_end_tower(self):
        self.move_disc_between_towers(self.tower_start, self.tower_end, self.tower_tmp, self.n_discs)


def main():
    logger.add_stdout_handler()
    log.info("Start app HanoiTowers. Solver uses recursion")

    hanoi_towers = HanoiTowers(5, to_log_moves=True)
    log.info(f"Initial state:\n{hanoi_towers}")

    hanoi_towers.move_discs_to_end_tower()

    log.info(f"State after processing:\n{hanoi_towers}")
    log.info("End app HanoiTowers")


if __name__ == "__main__":
    main()
