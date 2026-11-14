import numpy as np

def f_score(y_true, y_pred, beta):
    # Your code here
    true_len = len(y_true)
    pred_len = len(y_pred)

    if true_len == pred_len:

        true_positive = 0
        false_positive = 0
        false_negative = 0
        
        for i in range(true_len):
            if y_true[i] == 1 and y_true[i] == y_pred[i]:
                true_positive+=1
            if y_true[i] == 0 and y_pred[i] == 1:
                false_positive+=1
        if false_positive == 0 and true_positive == 0:
            return 0.0
        else: 
            precision = float(true_positive/(true_positive+false_positive))

        for i in range(true_len):
            if y_true[i] == 1 and y_pred[i] == 0:
                false_negative+=1
        if true_positive == 0 and false_negative == 0:
            return 0.0
        else: 
            recall = float(true_positive/(true_positive+false_negative))

        numerator = (1+beta**2)*(precision*recall)
        denominator = (beta**2*precision)+recall
        
        if denominator == 0:
            return 0
        else: 
            f_score = round(float(numerator/denominator),3)
            return f_score
    pass
