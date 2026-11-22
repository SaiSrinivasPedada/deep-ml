import numpy as np

def log_softmax(scores: np.ndarray) -> np.ndarray:
    # Your code here
    scores_length = len(scores)
    if scores_length != 0:

        sum_of_exps =  0
        for i in range(scores_length):
            sum_of_exps += np.exp(scores[i])
        log_of_sum = np.log(sum_of_exps)
        
        updated_list = []
        for i in range(scores_length):
            individual_value = 0
            individual_value = scores[i] - log_of_sum
            updated_list.append(individual_value)

        return updated_list
    
    else: 
        return -1

    pass