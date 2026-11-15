def calculate_f1_score(y_true, y_pred):

    true_len = len(y_true)
    pred_len = len(y_pred)

    true_positive = 0
    false_positive = 0
    false_negative = 0
    true_negative = 0

    for i in range(true_len):
        if y_true[i] == 1 and y_pred[i] == 1:
            true_positive+=1
        elif y_true[i] == 0 and y_pred[i] == 1:
            false_positive+=1
        elif y_true[i] == 1 and y_pred[i] == 0:
            false_negative+=1
        else: 
            true_negative+=1
    if true_positive+false_positive != 0:
        precision = true_positive/(true_positive+false_positive)
    else:
        precision = 0

    if true_positive+false_negative !=0: 
        recall = true_positive/(true_positive+false_negative)
    else:
        recall = 0
    
    if precision+recall !=0:
        f1 = float((2*precision*recall)/(precision+recall))
    else:
        f1 = 0
    
    return round(f1,3)