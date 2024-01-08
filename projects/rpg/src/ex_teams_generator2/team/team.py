
import random

from config.config import (
    ERROR_TAG,
    ERROR_NOT_ENOUGH_MSG,
    CALC_TEAM_MEMBER_MAX_TRIES,
    ERROR_MAX_TRIES_MSG,
    )
from config.config import log


def calc_team(team_name, names, names_sel, n_members):
    """Chooses n members randomly from a lists of names discarding names
    already selected from this team or previous teams.
    This implementation retries a max of times the random choose of a member
    when its name has already been selected.
    Also, removes temporally each member selected from the names,
    so it can accomplish the random selection without several tries.
    """
    log.info(f"Generate team: {team_name}")
    if len(names_sel) + n_members > len(names):
        log.warning(f"{ERROR_TAG}: {team_name}: {ERROR_NOT_ENOUGH_MSG}!")
        return {team_name: (ERROR_TAG, ERROR_NOT_ENOUGH_MSG)}
    members = []
    names_sel_set = set(names_sel)
    names_for_choosing = names[:]
    for _ in range(n_members):
        name = None
        selection_tries = 0
        while not name:
            name = random.choice(names_for_choosing)
            if name in names_sel_set:
                selection_tries += 1
                log.debug(f"Retry {selection_tries:3} when randomly selecting team member. Name already selected: {name}")
                if selection_tries >= CALC_TEAM_MEMBER_MAX_TRIES:
                    log.warning(f"{ERROR_TAG}: {team_name}: {ERROR_MAX_TRIES_MSG}!")
                    return {team_name: (ERROR_TAG, ERROR_MAX_TRIES_MSG % name)}
                name = None
                continue
            names_sel_set.add(name)
            names_sel += [name]
            members += [name]
            names_for_choosing.remove(name)
    log.info(f"{team_name} members: {members}")
    return {team_name: members}
