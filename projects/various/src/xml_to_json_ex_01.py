import json
import os
import pathlib
import time

from lxml import etree

from tools.logger.logger import log, add_stdout_handler
from tools.xml.xml_utils import parse_xml_obj_to_dict_filtered_by_tag

ROOT_FOLDER = pathlib.Path(__file__).parent.parent
RESOURCES_FOLDER = os.path.join(ROOT_FOLDER, 'res', 'data')
DATASET_FILE = os.path.join(RESOURCES_FOLDER, 'names_anime1.xml')

add_stdout_handler()


def load_data():
    with open(DATASET_FILE, encoding='utf-8') as fin:
        return ''.join(fin.readlines())


def main():
    start_time = time.perf_counter()
    data = load_data()
    root = etree.fromstring(data)
    animes = parse_xml_obj_to_dict_filtered_by_tag(root, tag_to_find='anime')

    log.info('-' * 15)
    log.info(json.dumps(animes))

    log.info('-' * 15)
    log.info(f"Animes: {len(animes['anime'])}")
    log.info(f'\nt: {time.perf_counter() - start_time:.{8}f} s')
    log.info('-' * 15)


if __name__ == '__main__':
    main()
