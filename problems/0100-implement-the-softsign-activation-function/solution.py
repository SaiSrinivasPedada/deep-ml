def softsign(x: float) -> float:
    result = x / (1+abs(x))
    return round(result, 4)