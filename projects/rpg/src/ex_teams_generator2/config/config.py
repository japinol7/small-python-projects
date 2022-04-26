import logging


GROUP_SEPARATOR = f"{'-' * 10}"
N_TEAMS = 42
N_MEMBERS = 3

N_TEAMS_MAX = 50
N_MEMBERS_MAX = 15

BODY_TEAMS_KEY = 'teams'
BODY_ERRORS_KEY = 'errors'

ERROR_TAG = 'Error'
ERROR_MAX_MSG = f"User input Error. Maximum {N_TEAMS_MAX} teams and {N_MEMBERS_MAX} members for team. " \
                f"Values must be numbers!"
ERROR_NOT_ENOUGH_MSG = 'Not enough Characters to generate this team'

CALC_TEAM_MEMBER_MAX_TRIES = 100
ERROR_MAX_TRIES_MSG = f"Max tries exceeded while choosing a team member: {CALC_TEAM_MEMBER_MAX_TRIES}. Name: %s"

LOGGER_FORMAT = '%(asctime)s %(levelname)s %(name)s: %(message)s'
logging.basicConfig(format=LOGGER_FORMAT)
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
