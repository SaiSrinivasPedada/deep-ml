import numpy as np

def pad_to(a: np.ndarray, j: int) -> np.ndarray:
    """Pad a with zeros (or truncate) to length j."""
    # Your code here
    a = a.tolist()
    length = len(a)
    if length>j:
        difference_1 = length-j
        for k in range(difference_1):
            a.pop(-1)
        return a
    elif length<j:
        difference_2 = j-length
        for i in range(difference_2):
            a.append(0.)
        return a
    else:
        return a
    pass