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
from matplotlib.ticker import FormatStrFormatter

import create_matrices
import find_teams_data
import calculate_opr_matrix
import error_methods

import matplotlib.pyplot as plt


# Create local variables using variables from create_matrices
match_data = create_matrices.match_data
team_numbers = create_matrices.team_numbers
total_scores = create_matrices.total_scores
total_matches = create_matrices.total_matches
total_teams = create_matrices.total_teams
teams_matrix = create_matrices.teams_matrix
score_vector = create_matrices.score_vector
match_data_for_error_reference = create_matrices.match_data_for_error_reference

# Create new empty arrays for graphing using total number of scores from match_data_for_error_reference
error_graph_array_y = np.zeros(2 * len(match_data_for_error_reference.index))
error_graph_array_x = np.zeros(2 * len(match_data_for_error_reference.index))


# _print_average_error_per_match calculates the average error between the real scores of a match and the predicted score
def print_average_error_per_match():
    # The sum of errors
    error_sum = 0
    # total_number_of_matches is used for the for loop
    total_number_of_matches = len(match_data_for_error_reference.index)
    # alliance_position is 1,2,or 3 for red alliance teams and 4,5, or 6 for blue alliance teams
    alliance_position = 1
    # alliance_score_position is 7 for red alliance and 8 for blue alliance
    alliance_score_position = 7
    # For loop iterates two times, once for each alliance
    for x in range(2):
        # For loop that iterates through total_number_of_matches
        for a in range(total_number_of_matches):
            # Set error_sum as the sum of difference between the sum of the predicted opr of teams
            # in the match and the true score and the previous error_sum
            error_sum = error_sum + find_teams_data.find_opr(match_data_for_error_reference.iloc[a, alliance_position]) \
                        + find_teams_data.find_opr(match_data_for_error_reference.iloc[a, alliance_position + 1]) \
                        + find_teams_data.find_opr(match_data_for_error_reference.iloc[a, alliance_position + 2]) \
                        - match_data_for_error_reference.iloc[a, alliance_score_position]
        # Set alliance_position as 4 for blue alliance teams
        alliance_position = 4
        # Set alliance_position as 8 for blue alliance scores
        alliance_score_position = 8
    # Initialize total_scores_from_error_reference to be the total number of scores from match_data_for_error_reference
    total_scores_from_error_reference = 2 * len(match_data_for_error_reference.index)
    # Divide the error sum by total_scores_from_error_reference and print
    print(error_sum/total_scores_from_error_reference)


# _print_largest_error iterates through each error per match for largest error, then prints
def print_largest_error():
    # Initialize largest_error as 0
    largest_error = 0
    # Initialize total_number_of_matches as length of match_data_for_error_reference
    total_number_of_matches = len(match_data_for_error_reference.index)
    # alliance_position is 1,2,or 3 for red alliance teams and 4,5, or 6 for blue alliance teams
    alliance_position = 1
    # alliance_score_position is 7 for red alliance and 8 for blue alliance
    alliance_score_position = 7
    # For loop iterates two times, once for each alliance
    for x in range(2):
        # For loop that iterates through total_number_of_matches
        for a in range(total_number_of_matches):
            # Set error_checker as the difference between the sum of the predicted opr of teams in the match
            # and the true score
            error_checker = find_teams_data.find_opr(match_data_for_error_reference.iloc[a, alliance_position]) \
                            + find_teams_data.find_opr(match_data_for_error_reference.iloc[a, alliance_position + 1]) \
                            + find_teams_data.find_opr(match_data_for_error_reference.iloc[a, alliance_position + 2]) \
                            - match_data_for_error_reference.iloc[a, alliance_score_position]
            # If the error_checker is larger than largest_error, set largest_error as error_checker value
            if error_checker > abs(largest_error):
                largest_error = error_checker
        # Set alliance_position as 4 for blue alliance teams
        alliance_position = 4
        # Set alliance_position as 8 for blue alliance scores
        alliance_score_position = 8
    # Print largest_error
    print(largest_error)


# _print_smallest_error iterates through each error per match for smallest error, then prints
def print_smallest_error():
    # Initialize smallest_error as 0
    smallest_error = 0
    # Initialize total_number_of_matches as length of match_data_for_error_reference
    total_number_of_matches = len(match_data_for_error_reference.index)
    # alliance_position is 1,2,or 3 for red alliance teams and 4,5, or 6 for blue alliance teams
    alliance_position = 1
    # alliance_score_position is 7 for red alliance and 8 for blue alliance
    alliance_score_position = 7
    # For loop iterates two times, once for each alliance
    for x in range(2):
        # For loop that iterates through total_number_of_matches
        for a in range(total_number_of_matches):
            # Set error_checker as the difference between the sum of the predicted opr of teams in the match
            # and the true score
            error_checker = find_teams_data.find_opr(match_data_for_error_reference.iloc[a, alliance_position]) \
                            + find_teams_data.find_opr(match_data_for_error_reference.iloc[a, alliance_position + 1]) \
                            + find_teams_data.find_opr(match_data_for_error_reference.iloc[a, alliance_position + 2]) \
                            - match_data_for_error_reference.iloc[a, alliance_score_position]
            # If the error_checker is smaller than smallest_error, set smallest_error as error_checker value
            if error_checker < abs(smallest_error):
                smallest_error = error_checker
        # Set alliance_position as 4 for blue alliance teams
        alliance_position = 4
        # Set alliance_position as 8 for blue alliance scores
        alliance_score_position = 8
    # Print smallest_error
    print(smallest_error)


# _graph_error graphs a histogram and normal distribution of the error data
def graph_error():
    # Initialize total_number_of_matches as length of match_data_for_error_reference
    total_number_of_matches = len(match_data_for_error_reference.index)
    # alliance_position is 1,2,or 3 for red alliance teams and 4,5, or 6 for blue alliance teams
    alliance_position = 1
    # alliance_score_position is 7 for red alliance and 8 for blue alliance
    alliance_score_position = 7
    # error_graph_array_counter is used to iterate through error_graph_array_y
    error_graph_array_counter = 0
    # For loop iterates two times, once for each alliance
    for x in range(2):
        # For loop that iterates through total_number_of_matches
        for a in range(total_number_of_matches):
            # Set current position in error_graph_array_y as the difference between the sum of
            # the predicted opr of teams in the match and the true score
            error_graph_array_y[error_graph_array_counter] = find_teams_data.find_opr(
                match_data_for_error_reference.iloc[a, alliance_position]) + find_teams_data.find_opr(
                match_data_for_error_reference.iloc[a, alliance_position + 1]) + find_teams_data.find_opr(
                match_data_for_error_reference.iloc[a, alliance_position + 2]) - match_data_for_error_reference.iloc[
                            a, alliance_score_position]
            # Set current position in error_graph_array_x as the value of the array counter. This is used to store the
            # "x-coordinate" of the error value.
            error_graph_array_x[error_graph_array_counter] = error_graph_array_counter
            # Increment error_graph_array_counter
            error_graph_array_counter = error_graph_array_counter + 1
        # Set alliance_position as 4 for blue alliance teams
        alliance_position = 4
        # Set alliance_position as 8 for blue alliance scores
        alliance_score_position = 8

    # Initialize fig and ax for
    fig, ax = plt.subplots()
    # Create histogram using error_graph_array_y data, 14 bins, yellow colour, and edge colour gray
    # Initialize counts, bins, and patches as values from this histogram
    counts, bins, patches = ax.hist(error_graph_array_y, bins=14, facecolor='yellow', edgecolor='gray')

    # Set the ticks to be at the edges of the bins.
    ax.set_xticks(bins)
    # Set the xaxis's tick labels to be formatted with 1 decimal place...
    ax.xaxis.set_major_formatter(FormatStrFormatter('%0.0f'))

    # Change the colors of bars at the edges...
    #twentyfifth, seventyfifth = np.percentile(error_graph_array_y, [25, 75])
    #for patch, rightside, leftside in zip(patches, bins[1:], bins[:-1]):
        #if rightside < twentyfifth:
            #patch.set_facecolor('green')
        #elif leftside > seventyfifth:
            #patch.set_facecolor('red')

    # Label the raw counts below the x-axis...
    bin_centers = 0.5 * np.diff(bins) + bins[:-1]
    for count, x in zip(counts, bin_centers):
        # Label the raw counts
        ax.annotate(str(int(count)), xy=(x, 0), xycoords=('data', 'axes fraction'),
                    xytext=(0, -18), textcoords='offset points', va='top', ha='center')

        # Label the percentages
        #percent = '%0.0f%%' % (100 * float(count) / counts.sum())
        #ax.annotate(percent, xy=(x, 0), xycoords=('data', 'axes fraction'),
                    #xytext=(0, -32), textcoords='offset points', va='top', ha='center')




    # Create more room at the bottom of the plot
    plt.subplots_adjust(bottom=0.15)
    # Set y label as 'Number In Bin'
    ax.set_ylabel('Number In Bin')

    # Fit a normal distribution to the data
    # Initialize mu as mean and std as standard deviation
    mu, std = norm.fit(error_graph_array_y)
    # Set xmin and xmax from plt data
    xmin, xmax = plt.xlim()
    # Set x as the linspace with parameters xmin, xmax, and 100
    x = np.linspace(xmin, xmax, 100)
    # Plot the PDF of the data using x, mu, and std
    p = norm.pdf(x, mu, std)

    # Generate twin axes of ax called ax2
    ax2 = ax.twinx()
    # Create y label for ax2 called 'Normal Distribution Scale' and colour blue
    ax2.set_ylabel('Normal Distribution Scale', color='tab:blue')
    # Plot normal distribution on ax2
    ax2.plot(x, p, 'k', linewidth=2)
    # Set the ticks on ax2 y axis as blue
    ax2.tick_params(axis='y', labelcolor='tab:blue')
    # Set ax2 bottom limit as 0
    ax2.set_ylim(bottom=0)
    # Set the graph to a tight layout, so the y-label of ax2 is not clipped
    fig.tight_layout(pad=2)
    # Temporary title for chart with mean and standard deviation
    title = "Fit results: mu = %.2f,  std = %.2f" % (mu, std)
    plt.title(title)

    # Plot the graph
    plt.show()
