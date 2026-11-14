import numpy as np
def precision(y_true, y_pred):
    # Your code here
    true_len = len(y_true)
    pred_len = len(y_pred)
    if true_len == pred_len:
        true_positive = 0
        false_positive = 0
        for i in range(true_len):
            if y_true[i] == 1 and y_true[i] == y_pred[i]:
                true_positive+=1
            if y_true[i] == 0 and y_pred[i] == 1:
                false_positive+=1
        if false_positive == 0 and true_positive == 0:
            return 0.0
        else: 
            precision = float(true_positive/(true_positive+false_positive))
            return precision
    pass
