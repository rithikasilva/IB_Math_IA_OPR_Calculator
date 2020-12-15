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











def graphErrorRough():
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



    fig, ax = plt.subplots()
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

    # Label the raw counts and the percentages below the x-axis...
    bin_centers = 0.5 * np.diff(bins) + bins[:-1]
    for count, x in zip(counts, bin_centers):
        # Label the raw counts
        ax.annotate(str(int(count)), xy=(x, 0), xycoords=('data', 'axes fraction'),
                    xytext=(0, -18), textcoords='offset points', va='top', ha='center')

        # Label the percentages
        #percent = '%0.0f%%' % (100 * float(count) / counts.sum())
        #ax.annotate(percent, xy=(x, 0), xycoords=('data', 'axes fraction'),
                    #xytext=(0, -32), textcoords='offset points', va='top', ha='center')




    # Give ourselves some more room at the bottom of the plot
    plt.subplots_adjust(bottom=0.15)
    ax.set_ylabel('Number In Bin')


    # Fit a normal distribution to the data:




    mu, std = norm.fit(error_graph_array_y)
    # Plot the PDF.
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, std)

    ax2 = ax.twinx()
    color = 'tab:blue'
    ax2.set_ylabel('Normal Distribution Scale', color=color)  # we already handled the x-label with ax1
    ax2.plot(x, p, 'k', linewidth=2)
    ax2.tick_params(axis='y', labelcolor=color)
    ax2.set_ylim(bottom=0)
    fig.tight_layout(pad=2)  # otherwise the right y-label is slightly clipped

    title = "Fit results: mu = %.2f,  std = %.2f" % (mu, std)
    plt.title(title)



    plt.show()