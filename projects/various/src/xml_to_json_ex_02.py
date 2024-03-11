import json
import os
import pathlib
import time

from lxml import etree

ROOT_FOLDER = pathlib.Path(__file__).parent.parent
RESOURCES_FOLDER = os.path.join(ROOT_FOLDER, 'res', 'data')
DATASET_FILE = os.path.join(RESOURCES_FOLDER, 'names_anime1.xml')
XSL_XML2JSON_FILE = os.path.join('utils', 'xml2json.xsl')


def load_xml_data(file_name):
    tree = etree.parse(file_name)
    xslt_root = etree.parse(XSL_XML2JSON_FILE)
    transform = etree.XSLT(xslt_root)
    res = transform(tree)
    return json.loads(str(res))


def main():
    animes = load_xml_data(DATASET_FILE)
    start_time = time.time()

    print('-' * 15)
    print(json.dumps(animes))

    print('-' * 15)
    print(f"Animes: {len(animes['animes'])}")
    print(f'\nt: {time.time() - start_time:.{8}f} s')
    print('-' * 15)


if __name__ == '__main__':
    main()
