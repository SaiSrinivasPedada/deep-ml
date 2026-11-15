from collections import Counter

def confusion_matrix(data):
    # Implement the function here
    data_len = len(data)
    true_positive = 0
    false_negative = 0
    false_positive = 0
    true_negative = 0
    for i in range(data_len):
        if data[i][0] == 1 and data[i][1] == 1:
            true_positive+=1
        elif data[i][0] == 1 and data[i][1] == 0:
            false_negative+=1
        elif data[i][0] == 0 and data[i][1] == 1:
            false_positive+=1
        else:
            true_negative+=1
    return [[true_positive,false_negative],[false_positive,true_negative]]
    pass
