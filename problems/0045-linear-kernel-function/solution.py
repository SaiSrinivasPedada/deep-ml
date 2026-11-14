import numpy as np

def kernel_function(x1, x2):
    # Your code here
    x1_length = len(x1)
    x2_length = len(x2)
    if x1_length == x2_length:
        dot_product = 0
        for i in range(x1_length):
            value = 0
            value = x1[i]*x2[i]
            dot_product+=value
        return dot_product
    else: return -1
    pass
