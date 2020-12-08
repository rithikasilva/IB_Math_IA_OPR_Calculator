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







os.system('python create_matrices.py')          #Creates score_matrix, teams_matrix, and match_data_for_error_reference


ans = True;
#While loop that displays a menu with options
while(ans):
    print("1. Calculate OPR")
    print("2. Predict OPR Score")
    print("3. Print Largest Error")
    print("4. Print Smallest Error")
    print("5. Print Average Error Per Match")
    print("6. Time to calculate opr matrix")
    print("7. Exit")

    choice = input("Please select a choice:")

    #Calculate the OPR of one team
    if choice == '1':
        try:
            team_choice = input("Please input a team number:")
            print(find_teams_data.findOPR('frc' + team_choice))
        except:
            print("Please input only team numbers of teams who competed in the events")

    # Calculate the OPR of three team
    if choice == '2':
        try:
            first_team_choice = input("Please input the first team number:")
            second_team_choice = input("Please input the second team number:")
            third_team_choice = input("Please input the third team number:")
            print(predictedScore('frc' + first_team_choice, 'frc' + second_team_choice, 'frc' + third_team_choice))
        except:
            print("Please input only team numbers of teams who competed in the events")
    #Calculate the largest error produced with reference event
    if choice == '3':
        error_methods.printLargestError()
    #Calculate the smallest error produced with reference event
    if choice == '4':
        error_methods.printSmallestError()
    #Calculate the average error produced with reference event
    if choice == '5':
        error_methods.printAvgErrorPerMatch()
    #Display the time taken to calculate OPR (specifically to create the OPR matrix)
    if choice == '6':
        print(calculate_opr_matrix.time_to_calculate)
    #Exit from menu
    if choice == '7':
        ans = False
    else:
        print("IN VALID INPUT")

