import numpy as np

def r_squared(y_true, y_pred):
    # Write your code here
    true_len = len(y_true)
    pred_len = len(y_pred)
    mean = float(sum(y_true)/len(y_true))

    if true_len == pred_len:

        rss = 0
        for i in range(true_len):
            value = 0
            value = ((y_true[i]-y_pred[i])**2)
            rss+=value
        
        tss = 0
        for i in range(true_len):
            value = 0
            value = ((y_pred[i]-mean)**2)
            tss+=value

        if tss == 0:
            return 0.0
        else:
            r_squared = 1 - (rss/tss)
            return r_squared

    pass
