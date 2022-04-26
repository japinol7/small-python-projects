
from config.config import (
    ERROR_TAG,
    ERROR_NOT_ENOUGH_MSG,
    ERROR_MAX_TRIES_MSG,
    )
from team.team import calc_team

TEAM_1_NAME = 'Team_01'
ERROR_RES_NOT_ENOUGH_CHARACTERS = {TEAM_1_NAME: (ERROR_TAG, ERROR_NOT_ENOUGH_MSG)}


def test_calc_team_1_member(team_names_resource, random_choice_names_mock):
    result = calc_team(team_name=TEAM_1_NAME, names=team_names_resource, names_sel=[], n_members=1)
    result_expected = {TEAM_1_NAME: ['Rei Ayanami']}
    assert result == result_expected


def test_calc_team_3_members(team_names_resource, random_choice_names_mock):
    result = calc_team(team_name=TEAM_1_NAME, names=team_names_resource, names_sel=[], n_members=3)
    result_expected = {TEAM_1_NAME: ['Rei Ayanami', 'Son Goku', 'Monokuma']}
    assert result == result_expected


def test_calc_team_no_members(team_names_resource, random_choice_names_mock):
    result = calc_team(team_name=TEAM_1_NAME, names=team_names_resource, names_sel=[], n_members=0)
    result_expected = {TEAM_1_NAME: []}
    assert result == result_expected


def test_calc_team_not_enough_names():
    result = calc_team(team_name=TEAM_1_NAME, names=['Name1', 'Name2'], names_sel=[], n_members=3)
    result_expected = ERROR_RES_NOT_ENOUGH_CHARACTERS
    assert result == result_expected


def test_calc_team_not_enough_names_already_sel():
    """Tests selecting 3 names from a list of 3 names, one of them already selected."""
    result = calc_team(team_name=TEAM_1_NAME,
                       names=['Name1', 'Name2', 'Name3'],
                       names_sel=['Name2'],
                       n_members=3)
    result_expected = ERROR_RES_NOT_ENOUGH_CHARACTERS
    assert result == result_expected


def test_calc_team_side_effect_names_sel():
    """Tests side effect of names selected."""
    names = ['Name1', 'Name2', 'Name3']
    names_sel = []
    calc_team(team_name=TEAM_1_NAME, names=names, names_sel=names_sel, n_members=2)
    assert all(item in names for item in names_sel) is True


def test_calc_team_side_effect_names_sel_once(random_choice_names_repeated_mock):
    """Tests side effect of names selected. It must select each name only once."""
    names = ['Rei Ayanami', 'Rei Ayanami', 'Son Goku', 'Monokuma']
    result = calc_team(team_name=TEAM_1_NAME, names=names, names_sel=['Rei Ayanami'], n_members=2)
    result_expected = {TEAM_1_NAME: ['Son Goku', 'Monokuma']}
    assert result == result_expected


def test_calc_2_teams_not_enough_names():
    """Tests selecting 1 name from a list of 3 names.
    Then, select 3 names from a list of 3 names, one of them already selected the fist time.
    """
    names = ['Name1', 'Name2', 'Name3']
    names_sel = []
    calc_team(team_name='Team_00', names=names, names_sel=names_sel, n_members=1)

    result = calc_team(team_name=TEAM_1_NAME, names=names, names_sel=names_sel, n_members=3)
    result_expected = ERROR_RES_NOT_ENOUGH_CHARACTERS
    assert result == result_expected


def test_calc_team_max_tries_exceeded(random_choice_names_all_repeated_mock):
    """Tests exceeding max tries when trying to choose a member team randomly."""
    names = ['Rei Ayanami', 'Rei Ayanami']
    result = calc_team(team_name=TEAM_1_NAME, names=names, names_sel=[], n_members=2)
    result_expected = {TEAM_1_NAME: (ERROR_TAG, ERROR_MAX_TRIES_MSG % 'Rei Ayanami')}
    assert result == result_expected
