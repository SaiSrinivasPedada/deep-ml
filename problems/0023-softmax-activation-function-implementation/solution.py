import math

def softmax(scores: list[float]) -> list[float]:
    if not scores:
        return []
    
    # Subtract the maximum score for numerical stability (prevents math range errors)
    max_score = max(scores)
    exp_scores = [math.exp(x - max_score) for x in scores]
    
    sum_exp_scores = sum(exp_scores)
    probabilities = [exp_x / sum_exp_scores for exp_x in exp_scores]
    
    return probabilities