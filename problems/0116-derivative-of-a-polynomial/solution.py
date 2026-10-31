def poly_term_derivative(c: float, x: float, n: float) -> float:
    # Your code here
    y = c*n*(x**(n-1))
    return y