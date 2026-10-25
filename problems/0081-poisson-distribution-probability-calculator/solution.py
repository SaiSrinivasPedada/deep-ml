import math

def poisson_probability(k, lambd, decimal_places=5):
    """
    Calculates Poisson probability and rounds to specified decimal places.
    k: number of occurrences (int)
    lambd: average rate (lambda) (float/int)
    """
    # Formula: (lambd^k * e^-lambd) / k!
    probability = (math.pow(lambd, k) * math.exp(-lambd)) / math.factorial(k)
    
    # Return formatted string with fixed decimal places
    return f"{probability:.{decimal_places}f}"