from collections import namedtuple

from tools.logger import logger
from tools.logger.logger import log
from stack import Stack

MIN_DISCS = 1
MAX_DISCS = 24

HanoiTowers_Move = namedtuple('hanoi_towers_move',
                              ['move_n', 'disc_n', 'tower_from', 'tower_to'])


class HanoiTowersException(Exception):
    pass


class HanoiTowers:
    """The Towers of Hanoi. This solver uses an iterative approach.
    Also, it is implemented as an iterator.
    """

    def __init__(self, n_discs, to_log_moves=False):
        self.n_discs = n_discs
        self.to_log_moves = to_log_moves
        self.tower_start = None
        self.tower_tmp = None
        self.tower_end = None
        self.move = 1
        self.total_moves = int(pow(2, self.n_discs) - 1)

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

        if self.n_discs % 2 == 0:
            self.tower_end, self.tower_tmp = self.tower_tmp, self.tower_end

    def __iter__(self):
        return self

    def __next__(self):
        if self.move > self.total_moves:
            raise StopIteration

        if self.move % 3 == 1:
            self.move_disc_between_towers(self.tower_start, self.tower_end, to_log=self.to_log_moves)
        elif self.move % 3 == 2:
            self.move_disc_between_towers(self.tower_start, self.tower_tmp, to_log=self.to_log_moves)
        elif self.move % 3 == 0:
            self.move_disc_between_towers(self.tower_tmp, self.tower_end, to_log=self.to_log_moves)

        self.move += 1

    def __str__(self):
        return f"HanoiTowers for n_discs: {self.n_discs}\n" \
               f"\ttower_start: {self.tower_start}\n" \
               f"\ttower_tmp: {self.tower_tmp if self.n_discs % 2 != 0 else self.tower_end}\n" \
               f"\ttower_end: {self.tower_end if self.n_discs % 2 != 0 else self.tower_tmp}"

    def move_disc_between_towers(self, tower1, tower2, to_log=False):
        no_disc_value = 0
        tower1_top_disc = tower1.peek() if not tower1.is_empty else no_disc_value
        tower2_top_disc = tower2.peek() if not tower2.is_empty else no_disc_value

        if tower1_top_disc == no_disc_value and tower2_top_disc == no_disc_value:
            raise Exception(f"No disc in towers: {tower1.name}, {tower2.name}")

        if tower1_top_disc == no_disc_value:
            ht_move = HanoiTowers_Move(self.move, tower2_top_disc, tower2.name, tower1.name)
            tower2.pop()
            tower1.push(tower2_top_disc)
        elif tower2_top_disc == no_disc_value:
            ht_move = HanoiTowers_Move(self.move, tower1_top_disc, tower1.name, tower2.name)
            tower1.pop()
            tower2.push(tower1_top_disc)
        elif tower1_top_disc <= tower2_top_disc:
            ht_move = HanoiTowers_Move(self.move, tower1_top_disc, tower1.name, tower2.name)
            tower1.pop()
            tower2.push(tower1_top_disc)
        else:
            ht_move = HanoiTowers_Move(self.move, tower2_top_disc, tower2.name, tower1.name)
            tower2.pop()
            tower1.push(tower2_top_disc)

        to_log and log.info(f"{ht_move.move_n:2}. Move disc {ht_move.disc_n} "
                            f"from {ht_move.tower_from} to {ht_move.tower_to}")


def main():
    logger.add_stdout_handler()
    log.info("Start app HanoiTowers. Solver uses iteration. Implemented as an iterator.")

    hanoi_towers = HanoiTowers(5, to_log_moves=True)
    log.info(f"Initial state:\n{hanoi_towers}")

    for _ in hanoi_towers:
        pass

    log.info(f"State after processing:\n{hanoi_towers}")
    log.info("End app HanoiTowers")


if __name__ == "__main__":
    main()
