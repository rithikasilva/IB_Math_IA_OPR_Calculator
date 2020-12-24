import csv
import os
import numpy as np
from numpy.linalg import inv
import scipy
import scipy.linalg
import pandas as pd
import time

import calculate_opr_matrix
import create_matrices

# Import in team_numbers from create_matrices
team_numbers = create_matrices.team_numbers


# _find_team finds the position of the specified team in the team_numbers DataFrame
def find_team(team_number):
    # iteration_static is used to iterate through all team_numbers
    iteration_static = len(team_numbers.columns)
    # iteration_dynamic is used to print out position of team_numbers
    iteration_dynamic = len(team_numbers.columns) - 1
    # For loop to iterate through the length of the team_numbers
    for x in range(iteration_static):
        # If the current position in team_numbers is the inputted team_number
        if team_numbers.iloc[0, iteration_dynamic] == team_number:
            # Return the value of iteration dynamic
            if iteration_dynamic is None:
                return
            else:
                return iteration_dynamic
        # Else, decrease iteration_dynamic by 1
        else:
            iteration_dynamic = iteration_dynamic - 1


# _find_opr finds opr of specified team from opr_matrix using _find_team() function
def find_opr(team):
    # Find and return the opr of specified team, if the team is found
    opr = calculate_opr_matrix.opr_matrix[find_team(team)]
    return opr


# _predicted_score predicts score of three specified teams using opr
def predicted_score(team1, team2, team3):
    # Find the opr of specified teams, add them together, then return score
    predicted_match_score = find_opr(team1) + find_opr(team2) + find_opr(team3)
    return predicted_match_score
