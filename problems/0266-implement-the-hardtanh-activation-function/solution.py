def hardtanh(x: float, min_val: float = -1.0, max_val: float = 1.0) -> float:
    
    if x > max_val:
        return max_val
    elif x>=0 and x<=max_val: 
        return x
    elif x<0 and x>=min_val:
        return x
    else:
        return min_val
    pass