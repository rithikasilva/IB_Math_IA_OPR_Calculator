import csv
import os
import numpy as np
from numpy.linalg import inv
import scipy
import scipy.linalg
import pandas as pd
import time

import create_matrices

start_time = time.time()
#OPR calculation using the equation:
# opr_matrix = (teams_matrix_transpose X teams_matrix)^-1 X teams_matrix_transpose X score_matrix
teams_matrix_transpose = create_matrices.teams_matrix.transpose()
#STRAIGHT UP CALC
opr_matrix = np.dot(np.dot(np.linalg.pinv(np.dot(teams_matrix_transpose, create_matrices.teams_matrix))
                           , teams_matrix_transpose), create_matrices.score_matrix)
time_to_calculate = time.time()- start_time


