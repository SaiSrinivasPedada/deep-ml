import numpy as np

def flip(a: np.ndarray) -> np.ndarray:
    """Reverse 1-D array a without slicing a[::-1]."""
    # Your code here
    l = len(a)-1
    m=l
    revised_list = []
    for i in range(l):
        y = float(a[m])
        revised_list.append(y)
        m=m-1
    z=float(a[0])
    revised_list.append(z)
    return revised_list
    pass