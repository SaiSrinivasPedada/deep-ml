import numpy as np

def eye(n: int) -> np.ndarray:
    """n x n identity matrix without np.eye."""
    # Your code here
    identity_matrix = []
    for i in range(n):
        internal_list = []
        for i in range(n):
            internal_list.append(0)
        identity_matrix.append(internal_list)
    for i in range(n):
        identity_matrix[i][i] = 1
    return identity_matrix 
    pass
