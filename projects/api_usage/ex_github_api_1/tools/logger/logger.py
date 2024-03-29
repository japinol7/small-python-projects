from datetime import datetime
import logging
import os
import sys

LOG_FILE = os.path.join('logs', f"log_{datetime.now().strftime('%Y-%m-%d_%H_%M_%S_%f')}.log")
LOG_FILE_UNIQUE = os.path.join('logs', "log.log")
SYS_STDOUT = sys.stdout

LOGGER_LEVEL = logging.INFO
LOGGER_FORMAT = '%(asctime)s.%(msecs)03d | %(levelname)s | %(message)s'
LOGGER_FORMAT_NO_DATE = 'No datetime | %(levelname)s | %(message)s'
LOGGER_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

log = logging.getLogger(__name__)
log.setLevel(LOGGER_LEVEL)


def add_stdout_handler(logger_format=LOGGER_FORMAT):
    stdout_handler = logging.StreamHandler(SYS_STDOUT)
    stdout_handler.setLevel(LOGGER_LEVEL)
    stdout_handler.setFormatter(logging.Formatter(fmt=logger_format, datefmt=LOGGER_DATE_FORMAT))
    log.addHandler(stdout_handler)


def add_file_handler(multiple_log_files=False, logger_format=LOGGER_FORMAT):
    if multiple_log_files:
        file_handler = logging.FileHandler(LOG_FILE, "w", encoding='UTF-8')
    else:
        file_handler = logging.FileHandler(LOG_FILE_UNIQUE, "w", encoding='UTF-8')

    file_handler.setLevel(LOGGER_LEVEL)
    file_handler.setFormatter(logging.Formatter(fmt=logger_format, datefmt=LOGGER_DATE_FORMAT))
    log.addHandler(file_handler)
