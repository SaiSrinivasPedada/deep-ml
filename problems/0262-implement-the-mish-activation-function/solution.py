import numpy as np

def mish(x: float) -> float:
    softplus = np.logaddexp(0, x)
    tanh = np.tanh(softplus)
    mish = x*tanh
    return mish
    pass