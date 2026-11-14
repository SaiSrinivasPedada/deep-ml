import numpy as np

def recall(y_true, y_pred):
    true_len = len(y_true)
    pred_len = len(y_pred)
    if true_len == pred_len:
        true_positive = 0
        false_negative = 0
        for i in range(true_len):
            if y_true[i] == 1 and y_true[i] == y_pred[i]:
                true_positive+=1
            if y_true[i] == 1 and y_pred[i] == 0:
                false_negative+=1
        if true_positive == 0 and false_negative == 0:
            return 0.0
        else: 
            recall = float(true_positive/(true_positive+false_negative))
            return recall
    pass
    pass
