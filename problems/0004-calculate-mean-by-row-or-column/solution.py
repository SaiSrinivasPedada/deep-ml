def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    if not matrix or not matrix[0]:
        return []
        
    # Find the row and column length of the matrix
    rows = len(matrix)
    columns = len(matrix[0])
    
    if mode == 'column':
        column_means = []
        for j in range(columns):
            # Sum all elements in the j-th column
            col_sum = sum(matrix[i][j] for i in range(rows))
            # Divide by the number of rows to get the mean
            column_means.append(col_sum / rows)
        return column_means
        
    elif mode == 'row':
        row_means = []
        for i in range(rows):
            # Sum all elements in the i-th row
            row_sum = sum(matrix[i])
            # Divide by the number of columns to get the mean
            row_means.append(row_sum / columns)
        return row_means
        
    else:
        raise ValueError("Mode must be either 'row' or 'column'")