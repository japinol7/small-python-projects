import json
import os
import pathlib
import time

from lxml import etree

ROOT_FOLDER = pathlib.Path(__file__).parent.parent
RESOURCES_FOLDER = os.path.join(ROOT_FOLDER, 'res', 'data')
DATASET_FILE = os.path.join(RESOURCES_FOLDER, 'names_anime1.xml')


def load_data():
    with open(DATASET_FILE, encoding='utf-8') as fin:
        return ''.join(fin.readlines())


def xml2dict(root, tag_to_find):
    children = root.findall(tag_to_find)

    def get_tags(children_):
        out = {}
        for child in list(children_):
            if len(list(child)):
                if child.tag not in out:
                    out[child.tag] = []
                out[child.tag].append(get_tags(child))
            else:
                out[child.tag] = child.text
                if child.attrib:
                    out[f"{child.tag}_attrib"] = {k: v for k, v in child.attrib.items()}
        return out
    return get_tags(children)


def main():
    start_time = time.time()
    data = load_data()
    root = etree.fromstring(data)
    animes = xml2dict(root, tag_to_find='anime')

    print('-' * 15)
    print(json.dumps(animes))

    print('-' * 15)
    print(f"Animes: {len(animes['anime'])}")
    print(f'\nt: {time.time() - start_time:.{8}f} s')
    print('-' * 15)


if __name__ == '__main__':
    main()
