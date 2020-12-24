import csv
import os
import numpy as np
from numpy.linalg import inv
import scipy
import scipy.linalg
import pandas as pd
import time

import create_matrices

# Record start_time to calculate total time required to calculate opr using one calculation with the normal equation
start_time = time.time()
# Create teams_matrix_transpose as transpose of teams_matrix from create_matrices
teams_matrix_transpose = create_matrices.teams_matrix.transpose()
# Create an opr_matrix using the normal equation. This can be represented in psuedocode as;
# opr_matrix = (teams_matrix_transpose X teams_matrix)^-1 X teams_matrix_transpose X score_matrix
opr_matrix = np.dot(np.dot(np.linalg.pinv(np.dot(teams_matrix_transpose, create_matrices.teams_matrix))
                           , teams_matrix_transpose), create_matrices.score_vector)
# Record total time to calculate opr_matrix as time_to_calculate
time_to_calculate = time.time()- start_time


