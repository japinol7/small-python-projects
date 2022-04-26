import json
import os

from config.config import (
    N_TEAMS,
    N_MEMBERS,
    GROUP_SEPARATOR,
    )
from config.config import log
from team.team import calc_team


FILE_NAMES = os.path.join('../..', 'res', 'names', 'names_anime1.json')


def main():
    names_sel = []

    with open(FILE_NAMES, 'r') as fin:
        names = json.loads(fin.read()).get('names', [])
    names = list(set(names))

    for i in range(N_TEAMS):
        calc_team(f'Team {i+1}', names, names_sel, N_MEMBERS)
        names = list(set(names) - set(names_sel))
        names_sel = []

    names_remaining = names
    if names_remaining:
        if len(names_remaining) < N_MEMBERS:
            new_ln = '\n'
            log.info(f"Remaining Characters:\n{new_ln.join([x for x in names])}\n{GROUP_SEPARATOR}")
        else:
            log.info(f"Remaining Characters: {len(names_remaining)}\n{GROUP_SEPARATOR}")


if __name__ == "__main__":
    main()
