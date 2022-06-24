import logging
import os

from version import version

APP_NAME = 'mazes'

MAZE_ROWS_COLS_MAX = 2000
MAZE_ROWS_COLS_MIN = 4

MAZE_ROWS_DEFAULT = 20
MAZE_COLUMNS_DEFAULT = 12
MAZE_SPARSENESS_ROWS_COLS_BASE = 12 * 12
MAZE_SPARSENESS_DEFAULT = 0.03
CELL_SEPARATOR = '  '

FILE_INPUT_PATH = os.path.join('..', 'input')
FILE_OUTPUT_PATH = os.path.join('..', 'output')

LOGGER_FORMAT = '%(asctime)s %(levelname)s %(name)s: %(message)s'
logging.basicConfig(format=LOGGER_FORMAT)
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

LOG_START_APP_MSG = f"Start app {APP_NAME} version: {version.get_version()}"
LOG_END_APP_MSG = f"End app {APP_NAME}"

LOG_INPUT_ERROR_MSG = "User input error. Terminating execution."
