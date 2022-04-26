import logging


GROUP_SEPARATOR = f"{'-' * 10}"
N_MEMBERS = 3
N_TEAMS = 42

ERROR_TAG = 'Error'
ERROR_NOT_ENOUGH_MSG = 'Not enough Characters to generate this team'

CALC_TEAM_MEMBER_MAX_TRIES = 100
ERROR_MAX_TRIES_MSG = f"Max tries exceeded while choosing a team member: {CALC_TEAM_MEMBER_MAX_TRIES}. Name: %s"

LOGGER_FORMAT = '%(asctime)s %(levelname)s %(name)s: %(message)s'
logging.basicConfig(format=LOGGER_FORMAT)
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
