import csv
import numpy as np
from numpy.linalg import inv
import scipy
import scipy.linalg
import pandas as pd
import time


# Create a pandas DataFrame with match data
match_data = pd.read_csv("OPR 2019 Ontario/Matches/combined_matches.csv", header=None)
# Create a pandas DataFrame with team involved in event
team_numbers = pd.read_csv("OPR 2019 Ontario/Teams/combined_teams.csv", header=None)
# Create a pandas DataFrame with data from 2019 provincial championship matches
match_data_for_error_reference = pd.read_csv("PROV CHAMP/2019oncmp_combined_matches.csv", header=None)

# total_scores is initialized as two times the length of match-data as there are two alliances in each match
total_scores = len(match_data)*2
# total_matches is initialized as length of match_data
total_matches = len(match_data)
# total_teams is initialized as number of columns in the list of teams csv
total_teams = len(team_numbers.columns)

# Generates empty matrix with total_scores x total teams dimensions
teams_matrix = np.zeros((total_scores, total_teams))
# Generates empty vector with 1 x total_scores dimensions
score_vector = np.zeros(total_scores)


# _populate_score_vector populates the score_vector with the scores from the matches
def populate_score_vector():
    # For loop that transfers the match scores into a 1 x total matches matrix
    # The red scores are first transferred, then the blue scores
    for x in range(total_scores):
        if x < total_scores/2:
            score_vector[x] = match_data.iloc[x, 7]
        else:
            score_vector[x] = match_data.iloc[x - total_matches, 8]


# _populate_teams_matrix populates the the teams_matrix with the data from match_data
def populate_teams_matrix():
    # match_data_row_counter
    match_data_row_counter = 0
    # matrix with teams and matches
    teams_matrix_row_counter = 0
    # match_data_colour_check_is_red used to check if there is still red team data left to convert into matrix
    match_data_colour_check_is_red = True
    # match_data_column_position is 1,2 or 3 for the red teams , and 4,5, or 6 for blue teams
    match_data_column_position = 1

    # For loop that repeats twice due to the two alliances
    for a in range(2):
        # For loop that iterates through rows of matches
        for b in range(total_matches):
            # For loop that iterates through each team on the alliance
            for c in range(3):
                # For loop to go through the total number of teams
                for d in range(total_teams):
                    # If the team in the current position in the team_numbers DataFrame is present in the match,
                    # Set the current position in the teams_matrix to 1 to indicate the teams existence in the match
                    if team_numbers.iloc[0 , d] == match_data.iloc[match_data_row_counter, match_data_column_position]:
                        teams_matrix[teams_matrix_row_counter , d] = 1
                # Move match_data_column_position to next team on alliance
                match_data_column_position = match_data_column_position + 1
            # Increment the row counter for the teams_matrix
            teams_matrix_row_counter = teams_matrix_row_counter + 1
            # If the match_data is still for red teams, reset match_data_column_position to 1,
            # otherwise set it to 4
            if match_data_colour_check_is_red:
                match_data_column_position = 1
            else:
                match_data_column_position = 4
            # Increment the row counter for match_data
            match_data_row_counter = match_data_row_counter + 1
        # Set match_data_colour_check_is_red to false for the blue teams
        match_data_colour_check_is_red = False
        # Reset the match_data_row_counter
        match_data_row_counter = 0


populate_score_vector()
populate_teams_matrix()
