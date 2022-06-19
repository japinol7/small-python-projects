import logging

from version import version

APP_NAME = 'mazes'

LOGGER_FORMAT = '%(asctime)s %(levelname)s %(name)s: %(message)s'
logging.basicConfig(format=LOGGER_FORMAT)
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

LOG_START_APP_MSG = f"Start app {APP_NAME} version: {version.get_version()}"
LOG_END_APP_MSG = f"End app {APP_NAME}"
