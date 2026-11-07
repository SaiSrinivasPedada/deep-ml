import numpy as np

def repeat_rows(a: np.ndarray, d: int) -> np.ndarray:
    """Stack d copies of 1-D array a as rows."""
    # Your code here
    list_ld = a.tolist()
    repeated_matrix = []
    for j in range(d):
        repeated_matrix.append(list_ld)
    return repeated_matrix
    pass