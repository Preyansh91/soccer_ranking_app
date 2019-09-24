import os
from collections import defaultdict, OrderedDict
import argparse
import logging


def get_games_list(game_list):
    """
    Split an input text file with one game per line into a list
    of games.

    :param game_list: input file with games results
    :return: list of games results
    """
    logging.info("Getting list of games from input file")
    games_played = []
    for line in game_list:
        game = line.rstrip().split(', ')
        games_played.append(game)

    return games_played


def compare_scores(games):
    """
    Assign rankings points to teams based on game outcome.
    Win: 3 points, Loss: 0 points, Draw: 1 point per team

    :param games: list of game results
    :return: dict of teams and its points
    based on games played
    """
    logging.info('Comparing scores for each game and assigning points')
    results = defaultdict(int)
    for game in games:
        result_1 = game[0].rsplit(',')
        team_1 = result_1[0].rsplit(' ', 1)
        team_1_name, team_1_score = team_1[0], team_1[1]

        result_2 = game[1].rsplit(',')
        team_2 = result_2[0].rsplit(' ', 1)
        team_2_name, team_2_score = team_2[0], team_2[1]

        if team_1_score > team_2_score:
            team_1_inc, team_2_inc = 3, 0
        elif team_1_score < team_2_score:
            team_1_inc, team_2_inc = 0, 3
        elif team_1_score == team_2_score:
            team_1_inc, team_2_inc = 1, 1

        results[team_1_name] += team_1_inc
        results[team_2_name] += team_2_inc
    return results


def sort_results(results):
    """
    Sort the team points dict

    :param results: dict of teams and its points
    based on games played
    :return: ordered dict in descending order
    """
    logging.info("Sorting results based on points")
    out = OrderedDict(sorted(results.items(), key=lambda x: x[0]))
    sorted_dict = OrderedDict(sorted(out.items(), key=lambda x: x[1], reverse=True))
    return sorted_dict


def generate_rankings(rankings_dict):
    """
    Generate ranks for teams based on
    points and output the result

    :param rankings_dict: ordered dict in
    descending order
    :return:
    """
    logging.info("Generate ranks based on points")
    count = 1
    current_rank_teams = 1
    with open('expected_output.txt', 'a') as fh:
        first_team, first_score = list(rankings_dict.keys())[0], list(rankings_dict.values())[0]
        fh.write('{}. {}, {} pts'.format(count, first_team, first_score))
        fh.write('\n')
        rankings_dict.popitem(last=False)
        for key, value in rankings_dict.items():
            if value == first_score:
                count += 0
                current_rank_teams += 1
            else:
                if current_rank_teams > 1:
                    count = count + current_rank_teams
                    current_rank_teams = 0
                else:
                    count += 1
            fh.write('{}. {}, {} pts'.format(count, key, value))
            fh.write('\n')
            first_score = value
            first_team = key
    with open('expected_output.txt', 'r') as fh:
        for line in fh:
            print(line)


def get_soccer_ranks_table(input_file_path):
    """
    Calls required methods to create rankings table

    :param input_file_path: Input file provided
    by user containing match results.
    :return:
    """
    try:
        with open(input_file_path, 'r') as fh:
            input = fh.readlines()
        games = get_games_list(input)
        results = compare_scores(games)
        rankings_dict = sort_results(results)
        generate_rankings(rankings_dict)
    except Exception as e:
        logging.error(e)
    finally:
        if os.path.exists("expected_output.txt"):
            os.remove("expected_output.txt")


if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
    logging.basicConfig(filename='{}/example.log'.format(dir_path), level=logging.DEBUG)
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file_path', type=str,
                        help="Get input file location on your environment with match results")
    args = parser.parse_args()
    if args.file_path:
        if os.path.exists(args.file_path):
            get_soccer_ranks_table(args.file_path)
        else:
            logging.error("Not able to find the input file in the location given")
    else:
        logging.error("Please provide an input file location")