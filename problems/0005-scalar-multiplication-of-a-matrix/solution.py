def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	# Your code here
	matrix_length = len(matrix[0])
	matrix_width = len(matrix)
	matrix_revised = []
	for i in range(matrix_length):
		list_revised=[]
		for j in range(matrix_width):
			revised_value = matrix[i][j]*scalar
			list_revised.append(revised_value)
		matrix_revised.append(list_revised)
	return matrix_revised
	pass