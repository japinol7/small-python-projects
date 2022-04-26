import os
import json
import pytest

os.environ['LOG_LEVEL'] = 'ERROR'

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))
)


@pytest.fixture(scope='session')
def json_event_resource():
    with open(os.path.join(__location__, 'test_files', 'test_event.json'), 'r') as json_file:
        raw = json.load(json_file)
    return raw


@pytest.fixture(scope='session')
def team_names_resource():
    with open(os.path.join(__location__, 'test_files', 'names_anime1.json'), 'r') as fin:
        names = json.loads(fin.read()).get('names', [])
    return list(set(names))
