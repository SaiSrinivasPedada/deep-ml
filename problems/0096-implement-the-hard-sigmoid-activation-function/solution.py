def hard_sigmoid(x: float) -> float:
    if x<=-3:
        return 0
    elif x>=3:
        return 1
    else:
        value = ((0.2)*x)+0.5
        return value
    pass