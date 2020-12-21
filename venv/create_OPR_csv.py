import csv
import find_teams_data
import create_matrices
import pandas as pd
import calculate_opr_matrix
import numpy as np




def sendOPRtoCsv():
    opr_data_for_csv = np.empty((create_matrices.total_teams,2), dtype="object")

    for x in range(create_matrices.total_teams):
        opr_data_for_csv[x, 0] = create_matrices.team_numbers.iloc[0, x]

    for y in range(create_matrices.total_teams):
        opr_data_for_csv[y, 1] = str(round(find_teams_data.findOPR(create_matrices.team_numbers.iloc[0, y]), 2))

    #df = pd.DataFrame(opr_data_for_csv, index=['Team Number', 'Offensive Power Rating'])
    df = pd.DataFrame(opr_data_for_csv, columns=['Team Number', 'Offensive Power Rating'])
    df.to_csv('OPR_DATA.csv')


