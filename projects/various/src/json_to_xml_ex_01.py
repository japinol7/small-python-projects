from datetime import datetime
import json
import os
import pathlib
import time

from tools.logger.logger import log, add_stdout_handler
from tools.xml.xml_utils import parse_listdict2xml, pformat_xml

MAX_ANIME_TO_FETCH = 2000

ROOT_FOLDER = pathlib.Path(__file__).parent.parent
RESOURCES_FOLDER = os.path.join(ROOT_FOLDER, 'res', 'data')
DATASET_FILE = os.path.join(RESOURCES_FOLDER, 'names_anime1.json')

ELEMENTS_WITH_ATTRIBUTES = {
    'id': {'date': datetime.now().strftime('%Y-%m-%d')},
    }

add_stdout_handler()


def load_data():
    animes = []
    with open(DATASET_FILE, encoding='utf-8') as fin:
        data = json.load(fin)
        for i, row in enumerate(data['names'][:MAX_ANIME_TO_FETCH], start=1):
            animes.append({
                'id': i,
                'name': row,
                })
    return animes


def main():
    animes = load_data()
    start_time = time.perf_counter()

    log.info('-' * 15)
    root = parse_listdict2xml(
        animes, root_name='npcs', element_name='npc',
        elements_with_attribs=ELEMENTS_WITH_ATTRIBUTES)
    log.info(pformat_xml(root))

    log.info('-' * 15)
    log.info(f"Animes: {len(animes)}")
    log.info(f'\nt: {time.perf_counter() - start_time:.{8}f} s')
    log.info('-' * 15)


if __name__ == '__main__':
    main()
