import numpy as np

def tanh(x: float) -> float:
    tanh = ((np.exp(x)-np.exp(-x))/(np.exp(x)+np.exp(-x)))
    return tanh
    pass