import numpy as np

def triu_ones(n: int) -> np.ndarray:
    uto_matrix = []
    initial_list = []
    for i in range(n):
        initial_list.append(0)
    for i in range(n):
        uto_matrix.append(initial_list)
    for i in range(n):
        for j in range(n):
            if i>=j:
                uto_matrix[i][j] = 1
    return uto_matrix
    pass