def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    a_length = len(a[0])
    a_width = len(a)
    revised_list_of_lists =[]
    for i in range(a_length):
        list_of_lists = []
        for j in range(a_width):
            list_of_lists.append(a[j][i])
        revised_list_of_lists.append(list_of_lists)
    return revised_list_of_lists
    pass