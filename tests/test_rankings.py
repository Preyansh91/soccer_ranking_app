from ranking_lib.rankings import *
from collections import OrderedDict

def test_get_games_list():
    game_list = [
        "Lions 3, Snakes 3\n",
        "Tarantulas 1, FC Awesome 0\n",
        "Lions 1, FC Awesome 1\n",
        "Tarantulas 3, Snakes 1\n",
        "Lions 4, Grouches 0\n"
    ]
    expected = [
        ['Lions 3', 'Snakes 3'],
        ['Tarantulas 1', 'FC Awesome 0'],
        ['Lions 1', 'FC Awesome 1'],
        ['Tarantulas 3', 'Snakes 1'],
        ['Lions 4', 'Grouches 0']
    ]
    game_list = get_games_list(game_list)
    assert game_list == expected


def test_compare_scores():
    games = [
        ['Lions 3', 'Snakes 3'],
        ['Tarantulas 1', 'FC Awesome 0'],
        ['Lions 1', 'FC Awesome 1'],
        ['Tarantulas 3', 'Snakes 1'],
        ['Lions 4', 'Grouches 0']
    ]
    expected = {
            'Tarantulas': 6,
            'FC Awesome': 1,
            'Snakes': 1,
            'Lions': 5,
            'Grouches': 0
        }
    result = compare_scores(games)
    assert expected == result


def test_sort_results():
    results = {
            'Tarantulas': 6,
            'FC Awesome': 1,
            'Snakes': 1,
            'Lions': 5,
            'Grouches': 0
        }
    expected = {
        'Tarantulas': 6,
        'Lions': 5,
        'FC Awesome': 1,
        'Snakes': 1,
        'Grouches': 0
    }
    out = sort_results(results)
    assert out == expected


