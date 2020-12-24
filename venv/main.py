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
import create_OPR_csv


os.system('python create_matrices.py')      # Creates score_matrix, teams_matrix, and match_data_for_error_reference

main_loop = True                            # Boolean that stores the state of the menu

# While loop that displays a menu with options
while main_loop:
    # Display menu with options
    print("1. Calculate OPR")
    print("2. Predict OPR Score")
    print("3. Print Largest Error")
    print("4. Print Smallest Error")
    print("5. Print Average Error Per Match")
    print("6. Time to calculate opr matrix")
    print("7. Graph")
    print("8. Send OPR data to csv")
    print("9. Exit")

    # Prompt for uer input
    choice = input("Please select a choice:")

    # Calculate the OPR of one team
    if choice == '1':
        # Ask for user input for team choice, then print calculated OPR
        try:
            team_choice = input("Please input a team number:")
            print("The OPR for " + str(team_choice) + " is " + str(find_teams_data.find_opr('frc' + team_choice)))
        # Print error prompt if input is invalid
        except:
            print("Please input only team numbers of teams who competed in the events")

    # Calculate the OPR of three team
    elif choice == '2':
        # Ask for three teams, then print the predicted score
        try:
            first_team_choice = input("Please input the first team number:")
            second_team_choice = input("Please input the second team number:")
            third_team_choice = input("Please input the third team number:")
            print("The predicted score is " + str(predicted_score('frc' + first_team_choice, 'frc' + second_team_choice, 'frc' + third_team_choice)))
        # Print error prompt if input is invalid
        except:
            print("Please input only team numbers of teams who competed in the events")

    # Calculate the largest error produced with reference event
    elif choice == '3':
        error_methods.print_largest_error()
    # Calculate the smallest error produced with reference event
    elif choice == '4':
        error_methods.print_smallest_error()
    # Calculate the average error produced with reference event
    elif choice == '5':
        error_methods.print_average_error_per_match()
    # Display the time taken to calculate OPR (specifically to create the OPR matrix)
    elif choice == '6':
        print(calculate_opr_matrix.time_to_calculate)
    # Display normal distribution and histogram of error data
    elif choice == '7':
        error_methods.graph_error()
    # Create csv with OPR Data
    elif choice == '8':
        create_OPR_csv.send_opr_to_csv()
    # Exit from menu
    elif choice == '9':
        main_loop = False
    # If input is invalid, print invalid input error message
    else:
        print("IN VALID INPUT")

