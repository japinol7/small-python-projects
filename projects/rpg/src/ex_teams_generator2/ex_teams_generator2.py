import json
import os

from config.config import (
    N_TEAMS,
    N_MEMBERS,
    GROUP_SEPARATOR,
    BODY_TEAMS_KEY,
    BODY_ERRORS_KEY,
    ERROR_TAG,
    LOG_START_APP_MSG,
    LOG_END_APP_MSG,
    )
from config.config import log
from team.team import calc_team
from utils.time_it_dec import time_it

FILE_NAMES = os.path.join('../..', 'res', 'names', 'names_anime1.json')


@time_it
def main():
    log.info(LOG_START_APP_MSG)

    with open(FILE_NAMES, 'r') as fin:
        names = json.loads(fin.read()).get('names', [])
    names = list(set(names))

    names_sel = []
    body = {BODY_TEAMS_KEY: {}, BODY_ERRORS_KEY: {}}
    log.info(f"Generate {N_TEAMS} Teams of {N_MEMBERS} members")
    for i in range(N_TEAMS):
        team_name = f'Team {i + 1}'
        team = calc_team(team_name, names, names_sel, N_MEMBERS)
        body_key = BODY_TEAMS_KEY if team.get(team_name)[0] != ERROR_TAG else BODY_ERRORS_KEY
        body[body_key].update(team)
        # remove currently selected member names from the list of available names
        names = list(set(names) - set(names_sel))
        names_sel = []

    names_remaining = names
    if names_remaining:
        if len(names_remaining) < N_MEMBERS:
            names_separator = ', '
            log.info(f"Remaining Characters: {names_separator.join([x for x in names])}\n{GROUP_SEPARATOR}")
        else:
            log.info(f"Remaining Characters: {len(names_remaining)}\n{GROUP_SEPARATOR}")

    log.info(LOG_END_APP_MSG)
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps(body),
        }


if __name__ == "__main__":
    res = main()
    log.info(res['body'])
