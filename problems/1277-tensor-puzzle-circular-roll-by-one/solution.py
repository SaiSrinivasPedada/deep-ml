import numpy as np

def roll(a: np.ndarray) -> np.ndarray:
    """Circular left shift by one."""
    # Your code here
    length = len(a)-1
    revised_list = []
    for i in range(length):
        y = float(a[i+1])
        revised_list.append(y)
    z = float(a[0])
    revised_list.append(z)
    return revised_list
    pass