import numpy as np
def activation_derivatives(x: float) -> dict[str, float]:
    sigmoid = 1 / (1 + np.exp(-x))
    der_sig = sigmoid*(1-sigmoid)
    der_tanh = 1-(np.tanh(x)**2)
    der_ReLU = 0
    if x > 0:
        der_ReLU = 1
    else: 
        der_ReLU = 0
    updated_list = {'sigmoid':der_sig, 'tanh':der_tanh, 'relu':der_ReLU}
    return updated_list
    pass