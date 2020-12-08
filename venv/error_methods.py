import csv
import os
import numpy as np
from numpy.linalg import inv
import scipy
import scipy.linalg
import pandas as pd
import time

import create_matrices
import find_teams_data
import calculate_opr_matrix
import error_methods


#________________________________________________________________

#Defines variables from creat_matrices file
match_data = create_matrices.match_data
team_numbers = create_matrices.team_numbers
total_scores = create_matrices.total_scores
total_matches = create_matrices.total_matches
total_teams = create_matrices.total_teams

teams_matrix = create_matrices.teams_matrix
score_matrix = create_matrices.score_matrix

match_data_for_error_reference = create_matrices.match_data_for_error_reference



def printAvgErrorPerMatch():
    error_sum = 0
    total_number_of_matches = len(match_data_for_error_reference.index)
    color_positions = 1
    colour_score_position = 7
    for x in range(2):
        for a in range(total_number_of_matches):
            error_sum = error_sum + find_teams_data.findOPR(match_data_for_error_reference.iloc[a, color_positions]) + find_teams_data.findOPR(match_data_for_error_reference.iloc[a, color_positions + 1]) + find_teams_data.findOPR(match_data_for_error_reference.iloc[a, color_positions + 2]) - match_data_for_error_reference.iloc[a, colour_score_position]
        color_positions = 4
        colour_score_position = 8
    total_scores = 2 * len(match_data_for_error_reference.index)
    print(error_sum/total_scores)


def printLargestError():
    error_checker = 0
    largest_error = 0
    total_number_of_matches = len(match_data_for_error_reference.index)
    color_positions = 1
    colour_score_position = 7
    for x in range(2):
        for a in range(total_number_of_matches):
            error_checker = find_teams_data.findOPR(match_data_for_error_reference.iloc[a, color_positions]) + find_teams_data.findOPR(match_data_for_error_reference.iloc[a, color_positions + 1]) + find_teams_data.findOPR(match_data_for_error_reference.iloc[a, color_positions + 2]) - match_data_for_error_reference.iloc[a, colour_score_position]
            if (error_checker > abs(largest_error)):
                largest_error = error_checker
        color_positions = 4
        colour_score_position = 8
    print(largest_error)


def printSmallestError():
    error_checker = 0
    smallest_error = 0
    total_number_of_matches = len(match_data_for_error_reference.index)
    color_positions = 1
    colour_score_position = 7
    for x in range(2):
        for a in range(total_number_of_matches):
            error_checker = find_teams_data.findOPR(match_data_for_error_reference.iloc[a, color_positions]) + find_teams_data.findOPR(match_data_for_error_reference.iloc[a, color_positions + 1]) + find_teams_data.findOPR(match_data_for_error_reference.iloc[a, color_positions + 2]) - match_data_for_error_reference.iloc[a, colour_score_position]
            if (error_checker < abs(smallest_error)):
                smallest_error = error_checker
        color_positions = 4
        colour_score_position = 8
    print(smallest_error)


