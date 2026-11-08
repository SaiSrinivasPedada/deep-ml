def reverse_linked_list(values, method="iterative"):
    # values: list of node values in head-to-tail order
    # method: 'iterative' or 'recursive'
    # return: list of node values after reversal
    value_length = len(values)
    j = value_length-1
    reverse_linked_list = []
    if method == "iterative" or "recursive":
        for i in range(value_length):
            reverse_linked_list.append(values[j])
            j=j-1
        return reverse_linked_list
    pass