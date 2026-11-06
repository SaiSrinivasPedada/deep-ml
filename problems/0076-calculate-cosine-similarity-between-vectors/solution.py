import numpy as np

def cosine_similarity(v1, v2):
	dot_product = 0
	v1_magnitude = 0
	v2_magnitude = 0
	v1_length = len(v1)
	v2_length = len(v2)
	if v1_length == v2_length:
		for i in range(v1_length):
			#Step 1 
			dot_product += v1[i]*v2[i]
			#Step 2 
			v1_magnitude += v1[i]**2
			v2_magnitude += v2[i]**2
		#Step 3
		cosine_sim = dot_product / ((v1_magnitude)**(1/2)*(v2_magnitude)**(1/2))
		return cosine_sim
	else: print("the inputs are not of same length")
	pass