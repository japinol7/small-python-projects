from datetime import datetime
import json
import os
import pathlib
import time

from lxml import etree

MAX_ANIME_TO_FETCH = 2000

ROOT_FOLDER = pathlib.Path(__file__).parent.parent
RESOURCES_FOLDER = os.path.join(ROOT_FOLDER, 'res', 'data')
DATASET_FILE = os.path.join(RESOURCES_FOLDER, 'names_anime1.json')

ELEMENTS_WITH_ATTRIBUTES = {
    'id': {'date': datetime.now().strftime('%Y-%m-%d')},
    }


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


def listdict2xml(animes):
    root = etree.Element('animes')
    for anime in animes:
        anime_ = etree.SubElement(root, 'anime')
        for k, v in anime.items():
            add_child_to_xml(anime_, k, attrib=ELEMENTS_WITH_ATTRIBUTES.get(k), text=str(v))
    return root


def pprint_xml(element, **kwargs):
    xml_ = etree.tostring(element, pretty_print=True, **kwargs)
    print(xml_.decode('utf-8'), end='')


def add_child_to_xml(parent, child_name, attrib=None, text=None):
    child = etree.SubElement(parent, child_name, attrib=attrib)
    child.text = str(text) if text else ''
    return child


def main():
    animes = load_data()
    start_time = time.perf_counter()

    print('-' * 15)
    root = listdict2xml(animes)
    pprint_xml(root)

    print('-' * 15)
    print(f"Animes: {len(animes)}")
    print(f'\nt: {time.perf_counter() - start_time:.{8}f} s')
    print('-' * 15)


if __name__ == '__main__':
    main()
