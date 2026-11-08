import numpy as np

def calculate_dot_product(vec1, vec2):
	vec1_length = len(vec1)
	vec2_length = len(vec2)
	dpc = 0
	for i in range(vec1_length):
		dpc+=vec1[i]*vec2[i]
	return dpc
	pass