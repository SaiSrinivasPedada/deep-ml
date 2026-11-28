import numpy as np
def thanksgiving_dish_predictor(preference_scores: list[float]) -> list[float]:
    # Your code here
    length = len(preference_scores)
    denominator = 0
    updated_list = []
    for i in range(length): 
        denominator += np.exp(preference_scores[i])
    for i in range(length):
        value = 0
        value = np.exp(preference_scores[i])
        value = (value/denominator)
        updated_list.append(value)
    return updated_list
    pass