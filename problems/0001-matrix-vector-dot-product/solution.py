def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	a_length = len(a[0])
	a_width = len(a)
	b_length = len(b)
	matrix_vector = []
	if a_length == b_length:
		for i in range(a_width):
			dot_product = 0
			for j in range(a_length):
				dot_product += a[i][j]*b[j]
			matrix_vector.append(dot_product)
		return matrix_vector
	else: return -1
	pass