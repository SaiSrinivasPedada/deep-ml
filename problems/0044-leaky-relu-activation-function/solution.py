def leaky_relu(z: float, alpha: float = 0.01) -> float|int:
    # Your code here
    if z == 0:
        return 0
    elif z > 0:
        return z
    else: 
        final_value = z*alpha
        return final_value
    pass
