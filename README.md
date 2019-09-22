# Soccer Ranking Table #

This app takes an input file containing the results of soccer matches played and prints out the ranking table of teams.

### How to run? ###
* Clone the repository and go inside the repository folder soccer_ranking_app
* First create a python 3.7 virtualenv and activate it from inside. Following are the steps to create virtual env: https://gist.github.com/pandafulmanda/730a9355e088a9970b18275cb9eadef3
* Install requirements by typing `pip install -e requirements.txt` from inside the soccer_rankings_app
* This app requires one command line argument which will contain the location of the input file from where the app is being run locally. Example:
`python ranking_lib/rankings.py -f ranking_lib/results_input.txt`
* Make sure you pass the right location of the file based on where it is locally. If the input file is in /Users/xyz/input.txt, then pass that location for the argument
parser file_path -f, like this: 
`python ranking_lib/rankings.py -f /Users/xyz/input.txt`
* To run the unit tests just run the following command from soccer_ranking_app folder:
`pytest -s -vv tests/`





