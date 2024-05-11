import json
import os
import pathlib
import time

from lxml import etree

from tools.logger.logger import log, add_stdout_handler

ROOT_FOLDER = pathlib.Path(__file__).parent.parent
RESOURCES_FOLDER = os.path.join(ROOT_FOLDER, 'res', 'data')
DATASET_FILE = os.path.join(RESOURCES_FOLDER, 'names_anime1.xml')
XSL_XML2JSON_FILE = os.path.join('tools', 'xml', 'xml2json.xsl')

add_stdout_handler()


def load_xml_data(file_name):
    tree = etree.parse(file_name)
    xslt_root = etree.parse(XSL_XML2JSON_FILE)
    transform = etree.XSLT(xslt_root)
    res = transform(tree)
    return json.loads(str(res))


def main():
    animes = load_xml_data(DATASET_FILE)
    start_time = time.perf_counter()

    log.info('-' * 15)
    log.info(json.dumps(animes))

    log.info('-' * 15)
    log.info(f"Animes: {len(animes['animes'])}")
    log.info(f'\nt: {time.perf_counter() - start_time:.{8}f} s')
    log.info('-' * 15)


if __name__ == '__main__':
    main()
