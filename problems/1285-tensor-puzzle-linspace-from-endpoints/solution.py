import numpy as np

def linspace(start, stop, n: int) -> np.ndarray:
    """n evenly spaced values from start to stop inclusive."""
    # Your code here
    if n>1:
        increment = (stop-start)/(n-1)
        linspace_list = []
        linspace_list.append(start)
        value = start
        for i in range(n-1):
            value = value+increment 
            linspace_list.append(value)
        return linspace_list
    else: return start
    pass