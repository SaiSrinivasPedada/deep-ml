import numpy as np
def softplus(x: float) -> float:
    val = np.log(1+np.exp(x))
    pass
    return round(val,4)