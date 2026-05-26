__author__ = 'Joan A. Pinol  (japinol)'

from simple_youtube.config import YOUTUBE_API_KEY
from simple_youtube.youtube_client import YoutubeClient
from tools.logger import logger
from tools.logger.logger import log
from tools.utils import utils
from version import version

logger.add_stdout_handler(logger_format=logger.LOGGER_FORMAT_NO_DATE)
logger.add_file_handler(logger_format=logger.LOGGER_FORMAT_NO_DATE)

APP_NAME = 'youtube_client_example_of_usage'

LOG_START_APP_MSG = f"Start app {APP_NAME} version: {version.get_version()}"
LOG_END_APP_MSG = f"End app {APP_NAME}"


def get_last_messages_from_live_stream(
        video_id, *, max_messages=None,
        filter_keywords=None, filter_out_keywords=None
    ):
    with YoutubeClient(
        api_key=utils.read_file_as_string(YOUTUBE_API_KEY),
        filter_keywords=filter_keywords,
        filter_out_keywords=filter_out_keywords,
    ) as client:
        client.get_live_chat_id(video_id)

        count = 1
        for item in client.iter_live_chat_messages(
            max_messages=max_messages,
            ):
            log.info(
                f"{count:4} "
                f"{item.author[:24]:24} "
                f"{item.message[:180]}")
            count += 1

        log.debug("EOF")


def main():
    log.info(LOG_START_APP_MSG)
    video_id = "video_id"

    get_last_messages_from_live_stream(
        video_id,
        max_messages=75,
        filter_keywords=[],
        filter_out_keywords=[],
        )

    log.info(LOG_END_APP_MSG)


if __name__ == "__main__":
    main()
