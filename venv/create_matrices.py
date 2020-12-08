import csv
import numpy as np
from numpy.linalg import inv
import scipy
import scipy.linalg
import pandas as pd
import time


#ONE EVENT CODE
match_data = pd.read_csv("OPR 2019 Ontario/Matches/combined_matches.csv", header = None) #header = none because there is no header for this CSV
team_numbers = pd.read_csv("OPR 2019 Ontario/Teams/combined_teams.csv", header = None) #header = none because there is no header for this CSV

match_data_for_error_reference = pd.read_csv("PROV CHAMP/2019oncmp_combined_matches.csv", header = None) #gets the data for a prov event



total_scores = len(match_data)*2 #this is because two alliances are playing per match
total_matches = len(match_data)
total_teams= len(team_numbers.columns) #gathers total teams from teams csv


teams_matrix = np.zeros((total_scores, total_teams)) #Generates empty matrix with total_scores x total teams dimensions
score_matrix = np.zeros(total_scores) #generates empty matrix with 1 x total_scores dimensions





def populateScoreMatrix():
    #for loop that transfers the match scores into a 1 x total matches matrix
    #The red scores are first transfered, then the blue scores
    for x in range(total_scores):
        if x < total_scores/2:
            score_matrix[x] = match_data.iloc[x, 7]

        else:
            score_matrix[x] = match_data.iloc[x - total_matches, 8]







def populateTeamsMatrix():
    #match_data list
    match_data_row_counter = 0
    #matrix with teams and matches
    teams_matrix_row_counter = 0
    match_data_colour_check_is_red = True
    match_data_column_counter_global = 1 #one for red, 4 for blue

    for a in range(2):
        #fills out the first half of the teams_matrix
        for b in range(total_matches): #iterates through the rows
            for c in range(3):#iterates through the teams in an alliance
                #checks whether the current position in the matrix corresponds to the teams in the allaince
                for d in range(total_teams):
                    if team_numbers.iloc[0 , d] == match_data.iloc[match_data_row_counter, match_data_column_counter_global]:
                        teams_matrix[teams_matrix_row_counter , d] = 1


                match_data_column_counter_global = match_data_column_counter_global + 1

            teams_matrix_row_counter = teams_matrix_row_counter + 1
            if (match_data_colour_check_is_red == True):
                match_data_column_counter_global = 1
            else:
                match_data_column_counter_global = 4
            match_data_row_counter = match_data_row_counter + 1

        match_data_colour_check_is_red = False
        match_data_row_counter = 0



populateScoreMatrix()
populateTeamsMatrix()