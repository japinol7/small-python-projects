import json
import os
import pathlib
import time
from pprint import pprint
from zipfile import ZipFile

ROOT_FOLDER = pathlib.Path(__file__).parent.parent
RESOURCES_FOLDER = os.path.join(ROOT_FOLDER, 'res', 'data')
DATASET_FOLDER_ZIP = os.path.join(RESOURCES_FOLDER, 'zip')
DATASET_FILE_ZIP = os.path.join(DATASET_FOLDER_ZIP, 'anime-offline-database.zip')


ANIME_TITLE_WANTED = (
    'detective conan',
    )

ANIME_TITLE_NOT_WANTED = (
    )

ANIME_TYPE_EXCLUDED_OLD = (
    'Movie',
    'Special',
    'OVA',
    'ONA',
    )

ANIME_TYPE_EXCLUDED = (
    'Special',
    )

ANIME_COLUMNS_WANTED = (
    'title',
    'year',
    'type',
    'animeSeason',
    'episodes',
    'picture',
    'sources',
    'status'  
    )


class ImportDataException(Exception):
    pass


def __unzip_data_file():
    print(f"Unzip data file")
    try:
        with ZipFile(DATASET_FILE_ZIP) as fin_zip:
            fin_zip.extractall(RESOURCES_FOLDER)
    except FileNotFoundError:
        raise ImportDataException(f"Error extracting data files. File not found: {DATASET_FILE_ZIP}")
    except Exception as e:
        raise ImportDataException(f"Error extracting data files from: {DATASET_FILE_ZIP}. Error msg: {e}")


def is_a_wanted_anime(anime, allow_missing_year=False):
    if not allow_missing_year and not anime['year']:
        return False
    if anime['type'] in (ANIME_TYPE_EXCLUDED):
        return False
    for item in ANIME_TITLE_NOT_WANTED:
        if item in anime['title'].lower():
            return False
    for item in ANIME_TITLE_WANTED:
        if item in anime['title'].lower():
            return True
    return False


def get_wanted_columns(anime):
    return {k: v for k, v in anime.items() if k in ANIME_COLUMNS_WANTED}


def main():
    __unzip_data_file()
    data_file_name = os.path.join('..', 'res', 'data', 'anime-offline-database.json')
    start_time = time.time()

    animes = []
    with open(data_file_name, encoding='utf-8') as fin:
        data = json.load(fin)
        for row in data['data']:
            row.update({
                'year': row['animeSeason'].get('year', 0) or 0
                })
            if not is_a_wanted_anime(row):
                continue
            row = get_wanted_columns(row)
            animes.append(row)

    animes.sort(key=lambda x: x['year'])
    for anime in animes:
        print('\n' * 3, '-' * 40, '\n')
        pprint(anime)

    print('-' * 40)
    print(f"Animes: {len(animes)}")
    print(f'\nt: {time.time() - start_time:.{8}f} s')
    print('-' * 15)


if __name__ == '__main__':
    main()
