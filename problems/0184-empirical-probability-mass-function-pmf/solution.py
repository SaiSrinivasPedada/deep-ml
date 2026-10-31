from collections import Counter

def empirical_pmf(samples):
    if not samples:
        return []
    
    total = len(samples)
    counts = Counter(samples)
    
    # Sort unique values by key in ascending order and calculate probabilities
    return [(val, counts[val] / total) for val in sorted(counts.keys())]