import numpy as np

def make_diagonal(x):
	x_length = len(x)
	revised_matrix = []
	for i in range(x_length):
		internal_list =[]
		for i in range(x_length):
			internal_list.append(0)
		revised_matrix.append(internal_list)
	for i in range(x_length):
		revised_matrix[i][i] = x[i]
	return revised_matrix
	pass