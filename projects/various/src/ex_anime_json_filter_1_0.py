import json
import os
import time
from pprint import pprint


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
    file_name = os.path.join('..', 'res', 'data', 'anime-offline-database.json')

    start_time = time.time()

    animes = []
    with open(file_name, encoding='UTF8') as fin:
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
