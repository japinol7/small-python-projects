import pytest


@pytest.fixture()
def random_choice_names_mock(mocker):
    mocker.patch("random.choice",
                 side_effect=('Rei Ayanami', 'Son Goku', 'Monokuma')
                 )


@pytest.fixture()
def random_choice_names_repeated_mock(mocker):
    mocker.patch("random.choice",
                 side_effect=('Rei Ayanami', 'Rei Ayanami', 'Son Goku', 'Monokuma')
                 )


@pytest.fixture()
def random_choice_names_all_repeated_mock(mocker):
    mocker.patch("random.choice", return_value='Rei Ayanami')
