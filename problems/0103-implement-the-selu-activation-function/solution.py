import numpy as np

def selu(x: float) -> float:
    alpha = 1.6732632423543772
    scale = 1.0507009873554804
    if x>0:
        return x*scale
    else: 
        value = alpha*scale*(np.exp(x)-1)
        return value
    pass