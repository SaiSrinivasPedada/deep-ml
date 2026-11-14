import numpy as np

def accuracy_score(y_true, y_pred):
    # Your code here
    true_len = len(y_true)
    pred_len = len(y_pred)
    if true_len == pred_len:
        counter = 0
        for i in range(true_len):
            if y_true[i] == y_pred[i]:
                counter+=1
        accuracy = float(counter/true_len)
        return accuracy
    else: return -1
    pass