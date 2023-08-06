from tools.logger import logger
from tools.logger.logger import log
from stack import Stack

MIN_DISCS = 1
MAX_DISCS = 24


class HanoiTowersException(Exception):
    pass


class HanoiTowers:
    """The Towers of Hanoi. This solver uses an iterative approach."""

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
        self.tower_start = Stack('tower_start')
        self.tower_tmp = Stack('tower_tmp')
        self.tower_end = Stack('tower_end')

        for disc in range(self.n_discs, 0, -1):
            self.tower_start.push(disc)

    def __str__(self):
        return f"HanoiTowers for n_discs: {self.n_discs}\n" \
               f"\ttower_start: {self.tower_start}\n" \
               f"\ttower_tmp: {self.tower_tmp}\n" \
               f"\ttower_end: {self.tower_end}"

    def move_disc_between_towers(self, tower1, tower2, to_log=False):
        no_disc_value = 0
        tower1_top_disc = tower1.pop() if not tower1.is_empty else no_disc_value
        tower2_top_disc = tower2.pop() if not tower2.is_empty else no_disc_value

        if tower1_top_disc == no_disc_value and tower2_top_disc == no_disc_value:
            raise Exception(f"No disc in towers: {tower1.name}, {tower2.name}")

        if tower1_top_disc == no_disc_value:
            to_log and log.info(f"{self.move:2}. Move disc {tower2_top_disc} from {tower2.name} to {tower1.name}")
            tower1.push(tower2_top_disc)
        elif tower2_top_disc == no_disc_value:
            to_log and log.info(f"{self.move:2}. Move disc {tower1_top_disc} from {tower1.name} to {tower2.name}")
            tower2.push(tower1_top_disc)
        elif tower1_top_disc <= tower2_top_disc:
            to_log and log.info(f"{self.move:2}. Move disc {tower1_top_disc} from {tower1.name} to {tower2.name}")
            tower2.push(tower2_top_disc)
            tower2.push(tower1_top_disc)
        else:
            to_log and log.info(f"{self.move:2}. Move disc {tower2_top_disc} from {tower2.name} to {tower1.name}")
            tower1.push(tower1_top_disc)
            tower1.push(tower2_top_disc)

    def move_discs_to_end_tower(self):
        start = self.tower_start
        end = self.tower_end
        tmp = self.tower_tmp

        total_moves = int(pow(2, self.n_discs) - 1)

        # Movement will be clockwise when the total discs is even, and anticlockwise otherwise
        if self.n_discs % 2 == 0:
            end, tmp = tmp, end

        for move in range(1, total_moves + 1):
            if move % 3 == 1:
                self.move_disc_between_towers(start, end, to_log=self.to_log_moves)
            elif move % 3 == 2:
                self.move_disc_between_towers(start, tmp, to_log=self.to_log_moves)
            elif move % 3 == 0:
                self.move_disc_between_towers(tmp, end, to_log=self.to_log_moves)
            self.move += 1


def main():
    logger.add_stdout_handler()
    log.info("Start app HanoiTowers. Solver uses iteration")

    hanoi_towers = HanoiTowers(5, to_log_moves=True)
    log.info(f"Initial state:\n{hanoi_towers}")

    hanoi_towers.move_discs_to_end_tower()
    log.info(f"State after processing:\n{hanoi_towers}")
    log.info("End app HanoiTowers")


if __name__ == "__main__":
    main()
