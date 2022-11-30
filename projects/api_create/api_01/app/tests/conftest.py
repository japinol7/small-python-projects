"""Define some fixtures to use in the project."""
import pytest
import json
from apistar import test

from app.app import app, animes


client = test.TestClient(app)


@pytest.fixture(scope='session')
def client_test():
    return client


@pytest.fixture(scope='session')
def animes_count_before_tests():
    return len(animes)


@pytest.fixture(scope='session')
def app_client_get_root():
    response = client.get('/')
    return response


@pytest.fixture(scope='session')
def app_client_get_all():
    response = client.get('/all')
    return response


@pytest.fixture(scope='session')
def app_client_post():
    anime_to_add = {
            'title': 'Fake Detective Conan',
            'year': 1995,
            'episodes': 12,
            'status': 'CURRENTLY',
            'type': 'TV',
            'animeSeason': {'season': 'fake_season', 'year': 1995},
            'picture': 'fake_picture',
            'sources': ['fake_source_01', 'fake_source_02']
            }
    response = client.post('/', json=json.loads(json.dumps(anime_to_add)))
    return response


@pytest.fixture(scope='session')
def app_client_post_second():
    anime_to_add = {
            'title': 'Fake 2 Detective Conan',
            'year': 1999,
            'episodes': 24,
            'status': 'CURRENTLY',
            'type': 'TV',
            'animeSeason': {'season': 'fake_season', 'year': 1999},
            'picture': 'fake_2_picture',
            'sources': ['fake_2_source_01', 'fake_2_source_02']
            }
    response = client.post('/', json=json.loads(json.dumps(anime_to_add)))
    return response


@pytest.fixture(scope='session')
def app_client_get():
    def make_app_client_get(anime_id):
        response = client.get(f'/{anime_id}/')
        return response
    return make_app_client_get


@pytest.fixture(scope='session')
def app_client_get_last_expected():
    return {'id': 63,
            'title': 'Detective Conan Movie 4: Captured In her Eyes',
            'year': 2000, 'episodes': 1,
            'status': 'UNKNOWN',
            'type': 'Movie',
            'animeSeason': {'season': 'UNDEFINED', 'year': 2000},
            'picture': 'https://anime-planet.com/images/anime/covers/detective-conan-movie-4-captured-in-her-eyes-1489.jpg',
            'sources': ['https://anime-planet.com/anime/detective-conan-movie-4-captured-in-her-eyes']}
