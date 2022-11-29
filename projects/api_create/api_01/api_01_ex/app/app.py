import json
import logging
import os

from apistar import App, Route, types, validators
from apistar.http import JSONResponse


logging.basicConfig(format='%(asctime)s %(levelname)s %(name)s: %(message)s')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

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
    'id',
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
    if anime['type'] in ANIME_TYPE_EXCLUDED:
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


def load_anime_data():
    file_name = os.path.join('res', 'data', 'anime-offline-database.json')
    animes = {}

    with open(file_name, encoding='UTF8') as fin:
        data = json.load(fin)
        for idx, row in enumerate(data['data']):
            row.update({
                'id': idx,
                'year': row['animeSeason'].get('year', 0) or 0,
                })
            if not is_a_wanted_anime(row):
                continue
            row = get_wanted_columns(row)
            animes[idx] = row
    return animes


animes = load_anime_data()
ANIME_VALID_STATUS = set([anime["status"] for anime in animes.values()])

ANIME_NOT_FOUND_MSG_ERROR = 'Anime not found'
ANIME_NOT_FOUND_LOG_ERROR = "Anime not found. Anime id: %s"


class Anime(types.Type):
    id = validators.Integer(allow_null=True)
    title = validators.String(max_length=2500)
    year = validators.Integer(minimum=1900, maximum=2050)
    episodes = validators.Integer(maximum=9999)
    status = validators.String(enum=list(ANIME_VALID_STATUS))
    type = validators.String(allow_null=True)
    animeSeason = validators.Object(allow_null=True)
    picture = validators.String(allow_null=True)
    sources = validators.Array(allow_null=True)


def list_anime_ids():
    logger.info(f'Get a list of all anime ids.')
    return [anime for anime in animes]


def list_animes():
    logger.info(f'Get all animes.')
    return [Anime(anime[1]) for anime in sorted(animes.items())]


def get_anime(anime_id):
    logger.info(f'Get anime with id: {anime_id}')
    try:
        anime_id = int(anime_id)
    except ValueError:
        logger.error(f'Value error: Anime id is not an integer: {anime_id}')

    anime = animes.get(anime_id)
    if not anime:
        logger.info(ANIME_NOT_FOUND_LOG_ERROR % anime_id)
        error = {'error': ANIME_NOT_FOUND_MSG_ERROR}
        return JSONResponse(error, status_code=404)

    return JSONResponse(Anime(anime), status_code=200)


def update_anime(anime_id, anime: Anime):
    logger.info(f'Update anime with id: {anime_id}')
    anime_id = int(anime_id)
    if not animes.get(anime_id):
        logger.info("Update Error. " + ANIME_NOT_FOUND_LOG_ERROR % anime_id)
        error = {'error': ANIME_NOT_FOUND_MSG_ERROR}
        return JSONResponse(error, status_code=404)

    anime.id = anime_id
    animes[anime_id] = dict(anime)
    return JSONResponse(Anime(anime), status_code=200)


def create_anime(anime: Anime):
    logger.info(f'Create anime with title: {anime.title}')
    anime_id = max(animes.keys()) + 1
    anime.id = anime_id
    animes[anime_id] = dict(anime)
    return JSONResponse(Anime(anime), status_code=201)


def delete_anime(anime_id):
    logger.info(f'Delete anime with id: {anime_id}')
    anime_id = int(anime_id)
    if not animes.get(anime_id):
        logger.info("Delete Error. " + ANIME_NOT_FOUND_LOG_ERROR % anime_id)
        error = {'error': ANIME_NOT_FOUND_MSG_ERROR}
        return JSONResponse(error, status_code=404)

    del animes[anime_id]
    return JSONResponse({}, status_code=204)


routes = [
    Route('/', method='GET', handler=list_anime_ids),
    Route('/all', method='GET', handler=list_animes),
    Route('/', method='POST', handler=create_anime),
    Route('/{anime_id}/', method='GET', handler=get_anime),
    Route('/{anime_id}/', method='PUT', handler=update_anime),
    Route('/{anime_id}/', method='DELETE', handler=delete_anime),
]

app = App(routes=routes)


if __name__ == '__main__':
    app.serve('127.0.0.1', 5000, debug=True)
