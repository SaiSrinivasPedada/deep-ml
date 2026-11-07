import numpy as np

def vstack(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Stack 1-D arrays a and b as rows of a (2, n) matrix."""
    # Your code here
    a = a.tolist()
    b = b.tolist()
    vertical_list = []
    vertical_list.append(a)
    vertical_list.append(b)
    return vertical_list
    pass