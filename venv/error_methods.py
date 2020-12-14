import csv
import os
import numpy as np
from numpy.linalg import inv
import scipy
import scipy.linalg
import pandas as pd
import time
from scipy import stats
from scipy.stats import norm


import create_matrices
import find_teams_data
import calculate_opr_matrix
import error_methods

import matplotlib.pyplot as plt


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

error_graph_array_y = np.zeros(2 * len(match_data_for_error_reference.index))
error_graph_array_x = np.zeros(2 * len(match_data_for_error_reference.index))

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

def graphError():
    total_number_of_matches = len(match_data_for_error_reference.index)
    color_positions = 1
    colour_score_position = 7
    error_graph_array_counter = 0
    for x in range(2):
        for a in range(total_number_of_matches):
            error_graph_array_y[error_graph_array_counter] = find_teams_data.findOPR(
                match_data_for_error_reference.iloc[a, color_positions]) + find_teams_data.findOPR(
                match_data_for_error_reference.iloc[a, color_positions + 1]) + find_teams_data.findOPR(
                match_data_for_error_reference.iloc[a, color_positions + 2]) - match_data_for_error_reference.iloc[
                            a, colour_score_position]
            error_graph_array_x[error_graph_array_counter] = error_graph_array_counter
            error_graph_array_counter = error_graph_array_counter + 1
        color_positions = 4
        colour_score_position = 8
    #plt.plot(error_graph_array_x,error_graph_array_y)

    #plt.ylim(0, 100)

    # Fit a normal distribution to the data:
    mu, std = norm.fit(error_graph_array_y)

    # Plot the histogram.
    plt.hist(error_graph_array_y, bins=14,density=True)





    plt.xticks()
    # Plot the PDF.
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, std)
    plt.plot(x, p, 'k', linewidth=2)
    title = "Fit results: mu = %.2f,  std = %.2f" % (mu, std)
    plt.title(title)




    plt.show()


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


