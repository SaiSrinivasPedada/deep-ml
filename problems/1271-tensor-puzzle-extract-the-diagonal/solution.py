import numpy as np

def diag(A: np.ndarray) -> np.ndarray:
    A_length = len(A[0])
    A_width = len(A)
    if A_length == A_width:
        A_diagonal = []
        for i in range(A_length):
            y = float(A[i][i])
            A_diagonal.append(y)
        return A_diagonal
    else: return FALSE
    pass
