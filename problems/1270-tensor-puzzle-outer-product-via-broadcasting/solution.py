import numpy as np

def outer(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Outer product of 1-D arrays a and b via broadcasting."""
    # Your code here
    a_length = len(a)
    b_length = len(b)
    revised_list = []
    for i in  range(a_length):
        internal_list = []
        for j in range(b_length):
            value = 0
            value = float(b[j]*a[i])
            internal_list.append(value)
        revised_list.append(internal_list)
    return revised_list
    pass
