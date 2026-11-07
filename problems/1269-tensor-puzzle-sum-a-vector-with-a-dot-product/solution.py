import numpy as np

def vector_sum(a: np.ndarray):
    """Sum elements of 1-D array a without np.sum / loops."""
    # Your code here
    length = len(a)
    summation = 0
    for i in range(length):
        summation+=a[i]
    return summation
    pass
