def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    determinant = (matrix[0][0]*matrix[1][1])-(matrix[0][1]*matrix[1][0])
    determinant_matrix = []
    if determinant!=0:
        first_term = matrix[1][1]/determinant 
        second_term = matrix[0][1]*(-1)/determinant
        third_term = matrix[1][0]*(-1)/determinant
        fourth_term = matrix[0][0]/determinant
    else: return ("None")
    first_row = [first_term,second_term]
    second_row = [third_term,fourth_term]
    return [first_row, second_row]

    pass