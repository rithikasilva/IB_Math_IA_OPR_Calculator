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

team_numbers = create_matrices.team_numbers
#Function to find the column number of the specified team in the teams csv file
def findTeam(team_number):
    iterationStatic = len(team_numbers.columns)
    iterationDynamic = len(team_numbers.columns) - 1
    for x in range(iterationStatic):
        if team_numbers.iloc[0,iterationDynamic] == team_number:
            if iterationDynamic == None:
                return
            else:
                return iterationDynamic
        else:
            iterationDynamic = iterationDynamic - 1



#print(predictedScore('frc2771','frc4476','frc7902'))
def findOPR(team):
    opr = calculate_opr_matrix.opr_matrix[findTeam(team)]
    return opr


#Function to add up an alliances predicted score using OPR
def predictedScore(team1, team2, team3):
    preditecScore = findOPR(team1) + findOPR(team2) + findOPR(team3)
    return preditecScore
