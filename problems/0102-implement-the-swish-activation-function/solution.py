import numpy as np
def swish(x: float) -> float:
    value = x*(1/(1+np.exp(-1*x)))
    return value
    pass