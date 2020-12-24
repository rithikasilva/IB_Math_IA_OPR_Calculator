import csv
import find_teams_data
import create_matrices
import pandas as pd
import calculate_opr_matrix
import numpy as np


# _send_opr_to_csv gathers opr data and creates csv file called "OPR_DATA.csv" with each team and calculated opr
def send_opr_to_csv():
    # Create empty total_teams x 2 array with objects as data type
    opr_data_for_csv = np.empty((create_matrices.total_teams, 2), dtype="object")

    # For loop that iterates through the number of total teams
    for x in range(create_matrices.total_teams):
        # Records team numbers into opr_data_for_csv array
        opr_data_for_csv[x, 0] = create_matrices.team_numbers.iloc[0, x]
    # For loop that iterates through the number of total teams
    for y in range(create_matrices.total_teams):
        # Records opr into opr_data_for_csv array
        opr_data_for_csv[y, 1] = str(round(find_teams_data.find_opr(create_matrices.team_numbers.iloc[0, y]), 2))

    # Create new pandas DataFrame  with opr_data_for_csv array data with 'Team Number' and 'Offensive Power Rating'
    # as column titles
    df = pd.DataFrame(opr_data_for_csv, columns=['Team Number', 'Offensive Power Rating'])
    # Create csv file called 'OPR_DATA.csv' with df as data
    df.to_csv('OPR_DATA.csv')


