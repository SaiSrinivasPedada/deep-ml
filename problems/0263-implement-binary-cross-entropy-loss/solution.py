import numpy as np
def binary_cross_entropy(y_true: list[float], y_pred: list[float], epsilon: float = 1e-15) -> float:
    length = len(y_true)
    mean = 0
    for i in range(length):
        mean += (-1)*(y_true[i]*np.log(y_pred[i])+(1-y_true[i])*np.log(1-y_pred[i]))
    mean = mean / length
    return round(mean,4)
    pass